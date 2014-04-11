# encoding: utf8
from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='Id', primary_key=True)),
                ('apikey', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Api Key', to_field='key_id', to='characters.ApiKey', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id', verbose_name='User')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('skillpoints', models.IntegerField(verbose_name='Skillpoints')),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                u'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
