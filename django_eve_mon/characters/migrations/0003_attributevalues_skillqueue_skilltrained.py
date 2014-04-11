# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_character'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeValues',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='characters.Character', to_field='id', verbose_name='Character')),
                ('attribute', models.ForeignKey(to='skills.Attribute', to_field=u'id', verbose_name='Attribute')),
                ('base', models.IntegerField(verbose_name='Base')),
                ('bonus', models.IntegerField(verbose_name='Bonus')),
            ],
            options={
                u'ordering': ['attribute__slot'],
                u'verbose_name_plural': 'Attribute Values',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillQueue',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='characters.Character', to_field='id', verbose_name='Character')),
                ('skillpoints', models.IntegerField(default=0, verbose_name='Skillpoints')),
                ('level', models.IntegerField(default=0, verbose_name='Level')),
                ('position', models.IntegerField(default=0, verbose_name='Position')),
                ('start_sp', models.IntegerField(default=0, verbose_name='Start Skillpoints')),
                ('end_sp', models.IntegerField(default=0, verbose_name='End Skillpoints')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillTrained',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='characters.Character', to_field='id', verbose_name='Character')),
                ('skillpoints', models.IntegerField(default=0, verbose_name='Skillpoints')),
                ('level', models.IntegerField(default=0, verbose_name='Level')),
            ],
            options={
                u'ordering': ['skill__name'],
                u'verbose_name_plural': 'Skills Trained',
            },
            bases=(models.Model,),
        ),
    ]
