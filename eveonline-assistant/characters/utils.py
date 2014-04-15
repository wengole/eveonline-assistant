from datetime import datetime

from braces.views import UserPassesTestMixin
from django.db import models


def points_per_second(primary_attribute, secondary_attribute):
    return (primary_attribute + (secondary_attribute / 2)) / 60

def timedelta_to_str(td):
    d = datetime(1, 1, 1) + td
    if d.month - 1 > 0:
        s = "%dm %dd %dh %dm %ds" % (d.month - 1, d.day - 1, d.hour, d.minute,
                                     d.second)
    elif d.day - 1 > 0:
        s = "%dd %dh %dm %ds" % (d.day - 1, d.hour, d.minute, d.second)
    elif d.hour > 0:
        s = "%dh %dm %ds" % (d.hour, d.minute, d.second)
    elif d.minute > 0:
        s = "%dm %ds" % (d.minute, d.second)
    else:
        s = "%ds" % (d.second)
    return s


class UserIsOwnerMixin(UserPassesTestMixin):

    def test_func(self, user):
        return self.get_object().is_owner(user) or self.request.user.is_staff


class SkillRelatedModel(models.Model):
    character = models.ForeignKey(
        'characters.Character',
        verbose_name='Character',
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        'skills.Skill',
        verbose_name='Skill',
        on_delete=models.CASCADE,
    )
    skillpoints = models.IntegerField('Skillpoints', default=0)
    level = models.IntegerField('Level', default=0)

    @property
    def sp_to_next_level(self):
        return self.skill.sp_to_level(self.level, self.level + 1) if self.level < 5 else 0

    class Meta:
        abstract = True