# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='skill',
            field=models.ForeignKey(to='skills.Skill', to_field='id', verbose_name='Skill'),
            preserve_default=True,
        ),
    ]
