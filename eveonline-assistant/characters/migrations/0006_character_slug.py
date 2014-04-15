# encoding: utf8
from django.db import migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_skilltrained_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False, null=True),
            preserve_default=False,
        ),
    ]
