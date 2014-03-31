from django.core.urlresolvers import reverse
from django.db import models


class ApiKey(models.Model):
    key_id = models.IntegerField('Key id', primary_key=True)
    verification_code = models.CharField('Verification code', max_length=255)
    user = models.ForeignKey(
        'users.User',
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='api_keys'
    )

    def is_owner(self, user):
        return self.user == user

    def __unicode__(self):
        return self.key_id


class Character(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    apikey = models.ForeignKey(
        'ApiKey',
        verbose_name='Api Key',
        on_delete=models.SET_NULL,
        related_name='characters_added',
        null=True
    )
    user = models.ForeignKey(
        'users.User',
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='characters'
    )
    name = models.CharField(
        'Name',
        max_length=255
    )
    skillpoints = models.IntegerField('Skillpoints')

    def get_absolute_url(self):
        return reverse('characters:detail', args=[str(self.id)])

    def is_owner(self, user):
        return self.user == user

    def __unicode__(self):
        return self.name


class SkillTrained(models.Model):
    character = models.ForeignKey(
        'Character',
        verbose_name="Character",
        on_delete=models.CASCADE,
        related_name='skills_known'
    )
    skill = models.ForeignKey(
        'skills.Skill',
        verbose_name="Skill",
        on_delete=models.CASCADE,
        related_name='characters_with_skill'
    )
    skillpoints = models.IntegerField("Skillpoints")
    level = models.IntegerField("Level")

    def __unicode__(self):
        return u"%s - %s L%d" % (self.character.name, self.skill.name, self.level)


class AttributeValues(models.Model):
    character = models.ForeignKey(
        'Character',
        verbose_name="Character",
        on_delete=models.CASCADE
    )
    attribute = models.ForeignKey(
        'skills.Attribute',
        verbose_name="Attribute",
        on_delete=models.CASCADE
    )
    base = models.IntegerField("Base")
    bonus = models.IntegerField("Bonus")

    def __unicode__(self):
        return u"%s - %s: %d" % (self.character, self.attribute.name, (self.base + self.bonus))