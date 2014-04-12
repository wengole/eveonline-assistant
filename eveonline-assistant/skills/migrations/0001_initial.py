# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='Id', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                u'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slot', models.IntegerField(verbose_name='Slot')),
            ],
            options={
                u'ordering': ['slot'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(verbose_name='Level')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='Id', primary_key=True)),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('group', models.ForeignKey(to='skills.Group', to_field='id', verbose_name='Group')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('description', models.TextField(verbose_name='Description')),
                ('primary_attribute', models.ForeignKey(to='skills.Attribute', to_field=u'id', verbose_name='Primary Attribute')),
                ('secondary_attribute', models.ForeignKey(to='skills.Attribute', to_field=u'id', verbose_name='Secondary Attribute')),
                ('required_skills', models.ManyToManyField(to='skills.Requirement', verbose_name='Required skills')),
            ],
            options={
                u'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
