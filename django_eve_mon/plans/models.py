from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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

    def add_skill(self, skill, level):
        existing_skill = self.character.has_skill(skill)
        if existing_skill and existing_skill.level < level - 1:
            return self.add_skill(skill, level - 1)
        elif existing_skill:
            return PlannedSkill.objects.create(
                plan=self,
                skill=skill,
                level=level
            )
        else:


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

    def __unicode__(self):
        return '%s: #%d %s L%d' % (
            self.plan,
            self.position,
            self.skill,
            self.level
        )

    class Meta:
        ordering = ['level']