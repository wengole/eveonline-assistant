# encoding: utf8
import autoslug.fields
from django.db import migrations
from slugify import slugify


def set_initial_slug(apps, schema_editor):
    Character = apps.get_model('characters', 'Character')
    for character in Character.objects.all():
        character.slug = slugify(character.name)
        character.save()


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_character_slug'),
    ]

    operations = [
        migrations.RunPython(set_initial_slug),
        migrations.AlterField(
            model_name='character',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
        ),
    ]
