# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('key_id', models.IntegerField(serialize=False, verbose_name='Key id', primary_key=True)),
                ('verification_code', models.CharField(max_length=255, verbose_name='Verification code')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id', verbose_name='User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
