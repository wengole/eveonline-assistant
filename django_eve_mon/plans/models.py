from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Max


class PlannedSkillManager(models.Manager):
    def create(self, **kwargs):
        plan = kwargs.get('plan')
        skill = kwargs.get('skill')
        level = kwargs.get('level')
        existing_skill = plan.character.has_skill(skill)
        if existing_skill.level == level:
            return existing_skill
        elif existing_skill.level == level - 1 or level == 1:
            return super(PlannedSkillManager, self).create(
                plan=plan,
                skill=skill,
                level=level,
                position=plan.next_position()
            )
        elif existing_skill:
            return self.create(
                plan=plan,
                skill=skill,
                level=level - 1,
                position=plan.next_position()
            )
        prerequisites = skill.required_skills.all()
        for pre_skill in prerequisites:
            self.create(
                plan=plan,
                skill=pre_skill.skill,
                level=pre_skill.level,
                position=plan.next_position()
            )
        return self.create(
            plan=plan,
            skill=skill,
            level=level,
            position=plan.next_position()
        )


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
        return self.skills.all().aggregate(Max('position'))['position__max'] + 1

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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(PlannedSkill, self).save(force_insert, force_update, using,
                                       update_fields)

    def __unicode__(self):
        return '%s: #%d %s L%d' % (
            self.plan,
            self.position,
            self.skill,
            self.level
        )

    class Meta:
        ordering = ['position']