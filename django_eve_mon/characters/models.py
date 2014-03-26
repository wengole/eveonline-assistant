from django.db import models


class ApiKey(models.Model):
    key_id = models.IntegerField("Key id", primary_key=True)
    verification_code = models.CharField("Verification code", max_length=255)

    def __unicode__(self):
        return self.key_id


class Character(models.Model):
    id = models.IntegerField("Id", primary_key=True)
    apikey = models.ForeignKey(
        'ApiKey',
        verbose_name="Api Key",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'users.User',
        verbose_name="User",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        "Name",
        max_length=255
    )
    skillpoints = models.IntegerField("Skillpoints")

    def __unicode__(self):
        return self.name


class SkillTrained(models.Model):
    character = models.ForeignKey(
        'Character',
        verbose_name="Character",
        on_delete=models.CASCADE
    )
    skill = models.ForeignKey(
        'skills.Skill',
        verbose_name="Skill",
        on_delete=models.CASCADE
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