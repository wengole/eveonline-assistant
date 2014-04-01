from decimal import Decimal
from braces.views import UserPassesTestMixin
from django.db import models


def points_per_second(primary_attribute, secondary_attribute):
    return (primary_attribute + (secondary_attribute / 2)) / 60


class UserIsOwnerMixin(UserPassesTestMixin):

    def test_func(self, user):
        return self.get_object().is_owner(user) or self.request.user.is_staff


class SkillRelatedModel(models.Model):
    character = models.ForeignKey(
        'characters.Character',
        verbose_name='Character',
        on_delete=models.CASCADE,
        related_name='skills_known'
    )
    skill = models.ForeignKey(
        'skills.Skill',
        verbose_name='Skill',
        on_delete=models.CASCADE,
    )
    skillpoints = models.IntegerField('Skillpoints')
    level = models.IntegerField('Level')

    @property
    def sp_to_next_level(self):
        return self.skill.skillpoints[self.level + 1] if self.level < 5 else self.skill.skillpoints[5]

    @property
    def primary_attribute_value(self):
        return Decimal(self.character.attributes.get(attribute=self.skill.primary_attribute).total)

    @property
    def secondary_attribute_value(self):
        return Decimal(self.character.attributes.get(attribute=self.skill.secondary_attribute).total)