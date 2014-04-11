# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plannedskill',
            name='skill',
            field=models.ForeignKey(to='skills.Skill', to_field='id', verbose_name='Skill'),
            preserve_default=True,
        ),
    ]
