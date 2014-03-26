from django.db import models


class Group(models.Model):
    id = models.IntegerField("Id", primary_key=True)
    name = models.CharField("Name", max_length=255)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    id = models.IntegerField("Id", primary_key=True)
    published = models.BooleanField("Published", default=True)
    group = models.ForeignKey(
        "Group",
        verbose_name="Group",
        on_delete=models.CASCADE
    )
    name = models.CharField("Name", max_length=255)
    rank = models.IntegerField("Rank")
    description = models.TextField("Description")
    required_skills = models.ManyToManyField(
        "Requirement",
        verbose_name="Required skills",
        related_name="provided_skills"
    )
    primary_attribute = models.ForeignKey(
        "Attribute",
        verbose_name="Primary Attribute",
        on_delete=models.CASCADE,
        related_name="primary_for"
    )
    secondary_attribute = models.ForeignKey(
        "Attribute",
        verbose_name="Secondary Attribute",
        on_delete=models.CASCADE,
        related_name="secondary_for"
    )

    def __unicode__(self):
        return self.name

    @property
    def skillpoints(self):
        return {
            1: 250 * self.rank,
            2: 1415 * self.rank,
            3: 8000 * self.rank,
            4: 45255 * self.rank,
            5: 256000 * self.rank,
        }


class Requirement(models.Model):
    skill = models.ForeignKey(
        "Skill",
        verbose_name="Skill",
        on_delete=models.CASCADE
    )
    level = models.IntegerField("Level")

    def __unicode__(self):
        return u"%s L%s" % (self.skill, self.level)


class Attribute(models.Model):
    name = models.CharField("Name", max_length=255)

    def __unicode__(self):
        return self.name
