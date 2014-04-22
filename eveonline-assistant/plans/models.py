from datetime import timedelta, datetime

from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Max
from django.utils.functional import cached_property

from characters.utils import timedelta_to_str
from core.utils import cacheable


class Plan(models.Model):
    name = models.CharField(
        'Name',
        blank=True,
        max_length=255
    )
    character = models.ForeignKey(
        'characters.Character',
        verbose_name='Character',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'users.User',
        verbose_name='User',
        on_delete=models.CASCADE
    )

    @property
    def next_position(self):
        cur_pos = self.skills.all().aggregate(Max('position'))['position__max']
        return cur_pos + 1 if cur_pos else 1

    def add_to_plan(self, skill, level):
        planned = self.skills.filter(skill=skill).last()
        known = self.character.skilltrained_set.get_or_none(skill=skill)
        if planned and planned.level >= level:
            return planned
        if known and known.level >= level:
            return known
        if planned or known:
            plan_level = planned.level if planned is not None else known \
                .level
            while level > plan_level:
                plan_level += 1
                PlannedSkill.objects.create(
                    plan=self,
                    skill=skill,
                    level=plan_level,
                    position=self.next_position
                )
            return
        prerequisites = [
            x for x in skill.required_skills.all() if self.character.has_skill(
                skill=x.skill
            ) is None or self.character.has_skill(skill=x.skill).level < x.level
        ]
        if prerequisites:
            for pre in prerequisites:
                self.add_to_plan(
                    skill=pre.skill,
                    level=pre.level
                )
        plan_level = 0
        while plan_level < level:
            plan_level += 1
            PlannedSkill.objects.create(
                plan=self,
                skill=skill,
                level=plan_level,
                position=self.next_position
            )
        return

    def get_absolute_url(self):
        return reverse('plans:detail', args=[str(self.id)])

    def __unicode__(self):
        return '%s: %s' % (self.character, self.name or 'Plan')


class PlannedSkill(models.Model):
    plan = models.ForeignKey(
        'Plan',
        verbose_name='Plan',
        on_delete=models.CASCADE,
        related_name='skills'
    )
    skill = models.ForeignKey(
        'skills.Skill',
        verbose_name='Skill',
        on_delete=models.CASCADE,
        related_name='in_plans'
    )
    level = models.IntegerField(
        'Level',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    position = models.IntegerField('Position')

    @cached_property
    def previous_skill(self):
        if self.position == 1:
            return None
        return PlannedSkill.objects.get(
            plan=self.plan,
            position=self.position - 1
        )

    @cached_property
    def character(self):
        """
        Quick access to the character of this skill
        """
        return self.plan.character

    @cached_property
    def training_time_td(self):
        """
        Calculate the time to train to this planned level from previous

        :return: The time to train to this planned skill level
        :rtype: timedelta
        """
        known = self.character.has_skill(skill=self.skill)
        if known and self.level == known.level + 1:
            return known.td_to_next_level
        pri_attr = self.character.attribute_value(self.skill.primary_attribute)
        sec_attr = self.character.attribute_value(self.skill.secondary_attribute)
        td = timedelta(seconds=self.skill.time_to_level(
            self.level - 1,
            self.level,
            pri_attr,
            sec_attr
        ))
        return td

    @cacheable('cumulative-td-{plan_id}-{skill_id}-{level}-{position}')
    def cumulative_training_time_td(self):
        td_total = timedelta()
        prev = self
        while True:
            if prev is None:
                break
            td_total += prev.training_time_td
            prev = prev.previous_skill
        return td_total

    @property
    def training_time(self):
        """
        Parse the training time timedelta to a string
        """
        return timedelta_to_str(self.training_time_td)

    @property
    def eta(self):
        """
        Return the current time plus timedelta
        """
        return datetime.utcnow() + self.cumulative_training_time_td()

    def __unicode__(self):
        return '%s: #%d %s L%d' % (
            self.plan,
            self.position,
            self.skill,
            self.level
        )

    class Meta:
        ordering = ['position']