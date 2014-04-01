from decimal import Decimal
from datetime import timedelta, datetime

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import models
from evelink.account import Account
from evelink.api import API
from evelink.char import Char
from core.utils import DjangoCache

from skills.models import Attribute
from skills.models import Skill


class ApiKey(models.Model):
    key_id = models.IntegerField('Key id', primary_key=True)
    verification_code = models.CharField('Verification code', max_length=255)
    user = models.ForeignKey(
        'users.User',
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='api_keys'
    )

    @property
    def api(self):
        return API(
            api_key=(self.key_id, self.verification_code),
            cache=DjangoCache()
        )

    def is_owner(self, user):
        return self.user == user

    def get_characters(self):
        account = Account(api=self.api)
        return account.characters().result

    def __unicode__(self):
        return "%s (%s)" % (
            self.key_id,
            self.characters_added.first().name
        )


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
    char_sheet_expires = models.DateTimeField(
        'Character Sheet Expiry',
        null=True
    )

    @property
    def char_api(self):
        return Char(self.id, self.apikey.api)

    @property
    def char_sheet(self):
        return self.char_api.character_sheet().result

    @property
    def char_sheet_expired(self):
        return self.char_sheet_expires < datetime.utcnow()

    def get_absolute_url(self):
        return reverse('characters:detail', args=[str(self.id)])

    def get_fetch_url(self):
        return reverse('characters:fetch', args=[str(self.id)])

    def update_character_sheet(self):
        message = {
            'status': messages.INFO,
            'text': '%s\'s character sheet cached until %s' % (
                self.name,
                self.char_sheet_expires
            )
        }
        if not self.char_sheet_expired:
            return message
        if self._update_attributes() and self._update_skills():
            message['status'] = messages.SUCCESS
            message['text'] = 'Updated %s\'s character sheet successfully' % \
                self.name
            return message
        message['status'] = messages.ERROR
        message['text'] = 'Failed to update %s\'s character sheet' % self.name
        return message

    def _update_attributes(self):
        sheet_attributes = self.char_sheet['attributes']
        for attr in sheet_attributes:
            attribute = Attribute.objects.get(name=attr)
            attr_value, _ = AttributeValues.objects.get_or_create(
                character=self,
                attribute=attribute,
                defaults={
                    'base': 0,
                    'bonus': 0
                }
            )
            attr_value.base = sheet_attributes[attr]['base']
            bonus_val = sheet_attributes[attr].get('bonus')
            if bonus_val is not None:
                attr_value.bonus = bonus_val['value']
            attr_value.save()
        # TODO: Catch exception and return False
        return True

    def _update_skills(self):
        skills = self.char_sheet['skills']
        for skill in skills:
            skl = Skill.objects.get(id=skill['id'])
            skl_lvl, _ = SkillTrained.objects.get_or_create(
                character=self,
                skill=skl,
                defaults={
                    'skillpoints': 0,
                    'level': 0
                }
            )
            skl_lvl.skillpoints = skill['skillpoints']
            skl_lvl.level = skill['level']
            skl_lvl.save()
        # TODO: Catch exception and return False
        return True

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

    @property
    def sp_to_next_level(self):
        return self.skill.skillpoints[self.level + 1] if self.level < 5 else self.skill.skillpoints[5]

    @property
    def primary_attribute_value(self):
        return Decimal(self.character.attributes.get(attribute=self.skill.primary_attribute).total)

    @property
    def secondary_attribute_value(self):
        return Decimal(self.character.attributes.get(attribute=self.skill.secondary_attribute).total)

    @property
    def time_to_next_level(self):
        if self.level == 5:
            return 0
        seconds = (self.sp_to_next_level - self.skillpoints) / self.skill.points_per_second(
            self.primary_attribute_value,
            self.secondary_attribute_value
        )
        return str(timedelta(seconds=int(seconds)))

    @property
    def progress(self):
        if self.level == 5:
            return Decimal(100)
        start = Decimal(self.skillpoints - self.skill.skillpoints[self.level])
        end = Decimal(self.sp_to_next_level - self.skill.skillpoints[self.level])
        if end == 0:
            return Decimal(0)
        return (start / end) * 100

    def __unicode__(self):
        return u"%s - %s L%d" % (self.character.name, self.skill.name, self.level)


class AttributeValues(models.Model):
    character = models.ForeignKey(
        'Character',
        verbose_name="Character",
        on_delete=models.CASCADE,
        related_name='attributes'
    )
    attribute = models.ForeignKey(
        'skills.Attribute',
        verbose_name="Attribute",
        on_delete=models.CASCADE
    )
    base = models.IntegerField("Base")
    bonus = models.IntegerField("Bonus")

    @property
    def total(self):
        return self.base + self.bonus

    def __unicode__(self):
        return u"%s - %s: %d" % (self.character, self.attribute.name, (self.base + self.bonus))

    class Meta:
        ordering = ['attribute__slot']