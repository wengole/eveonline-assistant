from django.db import models


class Group(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    name = models.CharField('Name', max_length=255)

    def __unicode__(self):
        return self.name

    @property
    def has_published_skills(self):
        return len(self.skills.filter(published=True)) > 0

    class Meta:
        ordering = ['name']


class Skill(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    published = models.BooleanField('Published', default=True)
    group = models.ForeignKey(
        'Group',
        verbose_name='Group',
        on_delete=models.CASCADE,
        related_name='skills'
    )
    name = models.CharField('Name', max_length=255)
    rank = models.IntegerField('Rank')
    description = models.TextField('Description')
    required_skills = models.ManyToManyField(
        'Requirement',
        verbose_name='Required skills',
        related_name='provided_skills',
        blank=True
    )
    primary_attribute = models.ForeignKey(
        'Attribute',
        verbose_name='Primary Attribute',
        on_delete=models.CASCADE,
        related_name='primary_for'
    )
    secondary_attribute = models.ForeignKey(
        'Attribute',
        verbose_name='Secondary Attribute',
        on_delete=models.CASCADE,
        related_name='secondary_for'
    )

    @property
    def skillpoints(self):
        return {
            0: 0,
            1: 250 * self.rank,
            2: 1415 * self.rank,
            3: 8000 * self.rank,
            4: 45255 * self.rank,
            5: 256000 * self.rank,
        }

    def sp_to_level(self, from_level=0, to_level=1):
        """
        Calculate the skillpoint requirement from one level to another
        :param from_level: int start level
        :param to_level: int end level
        :return: skillpoint total
        :rtype: int
        """
        total = self.skillpoints[to_level] - self.skillpoints[from_level]
        return total

    def time_to_level(self, from_level=0, to_level=1, pri_attr_value=1,
                      sec_attr_value=1):
        """
        Calculate the time taken to get from one level to another
        :param from_level: int start level
        :param to_level: int end level
        :param pri_attr_value: the primary attribute value for the calculation
        :param sec_attr_value: the secondary attribute value for the calculation
        :return: The number of seconds this training will take
        :rtype: int
        """
        sp = self.sp_to_level(from_level, to_level)
        points_per_second = (pri_attr_value + (sec_attr_value / 2)) / 60
        return int(sp / points_per_second)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Requirement(models.Model):
    skill = models.ForeignKey(
        'Skill',
        verbose_name='Skill',
        on_delete=models.CASCADE
    )
    level = models.IntegerField('Level')

    def __unicode__(self):
        return u'%s L%s' % (self.skill, self.level)


class Attribute(models.Model):
    name = models.CharField('Name', max_length=255)
    slot = models.IntegerField('Slot')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['slot']
