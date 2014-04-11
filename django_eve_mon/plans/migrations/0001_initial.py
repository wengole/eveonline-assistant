# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0003_attributevalues_skillqueue_skilltrained'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name', blank=True)),
                ('character', models.ForeignKey(to='characters.Character', to_field='id', verbose_name='Character')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id', verbose_name='User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlannedSkill',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan', models.ForeignKey(to='plans.Plan', to_field=u'id', verbose_name='Plan')),
                ('level', models.IntegerField(verbose_name='Level', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('position', models.IntegerField(verbose_name='Position')),
            ],
            options={
                u'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
    ]
