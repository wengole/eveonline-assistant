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
        "self",
        verbose_name="Required skills",
        related_name="provided_skills"
    )
    primary_attribute = models.ForeignKey(
        "Attribute",
        verbose_name="Attribute",
        on_delete=models.CASCADE
    )
    secondary_attribute = models.ForeignKey(
        "Attribute",
        verbose_name="Attribute",
        on_delete=models.CASCADE
    )

    def __unicode__(self):
        return self.name


class Attribute(models.Model):
    id = models.IntegerField("Id", primary_key=True)
    name = models.CharField("Name", max_length=255)

    def __unicode__(self):
        return self.name
