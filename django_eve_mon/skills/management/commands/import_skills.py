from django.core.management import BaseCommand
from evelink.eve import EVE
from django_eve_mon.skills.models import Group, Skill, Requirement, Attribute


class Command(BaseCommand):
    args = ""
    help = ""

    def handle(self, *args, **options):
        eve = EVE()
        r = eve.skill_tree()
        skills = {}
        for group in r[0].values():
            grp = Group(
                id=group['id'],
                name=group['name']
            )
            grp.save()
            for skill in group['skills'].values():
                skills[skill['id']] = skill
                skl = Skill(
                    id=skill['id'],
                    name=skill['name'],
                    published=skill['published'],
                    rank=skill['rank'],
                    description=skill['description'],
                    group=grp,
                )
                attr, _ = Attribute.objects.get_or_create(
                    name=skill['attributes']['primary'] or ''
                )
                skl.primary_attribute = attr
                attr, _ = Attribute.objects.get_or_create(
                    name=skill['attributes']['secondary'] or ''
                )
                skl.secondary_attribute = attr
                skl.save()

        for skill in skills.values():
            skl = Skill.objects.get(id=skill['id'])
            for req_skill in skill['required_skills'].values():
                rskl = Skill.objects.get(id=req_skill['id'])
                requirement, _ = Requirement.objects.get_or_create(
                    skill=rskl,
                    level=req_skill['level']
                )
                skl.required_skills.add(requirement)
                skl.save()