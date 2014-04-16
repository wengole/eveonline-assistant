from characters.models import SkillTrained
from core.tests import BaseTest
from plans.forms import PlanForm
from plans.models import PlannedSkill
from skills.models import Skill


class TestPlan(BaseTest):
    fixtures = ['skills', ]

    def test_create_plan(self):
        # Ensure the form for creating a plan only lists user's characters
        form = PlanForm(
            self.user1
        )
        char_field = form.fields['character']
        self.assertTrue(self.character1 in char_field.queryset)
        self.assertFalse(self.character2 in char_field.queryset)

    def test_add_to_plan(self):
        # Add a skill with requirements to the plan and ensure the planned
        # skills are correct
        skill = Skill.objects.get(name='Armor Layering')
        self.plan1.add_to_plan(
            skill=skill,
            level=2
        )
        expected = [
            repr(PlannedSkill(
                plan=self.plan1,
                skill=Skill.objects.get(name='Mechanics'),
                level=1,
                position=1
            )),
            repr(PlannedSkill(
                plan=self.plan1,
                skill=Skill.objects.get(name='Mechanics'),
                level=2,
                position=2
            )),
            repr(PlannedSkill(
                plan=self.plan1,
                skill=Skill.objects.get(name='Mechanics'),
                level=3,
                position=3
            )),
            repr(PlannedSkill(
                plan=self.plan1,
                skill=Skill.objects.get(name='Armor Layering'),
                level=1,
                position=4
            )),
            repr(PlannedSkill(
                plan=self.plan1,
                skill=Skill.objects.get(name='Armor Layering'),
                level=2,
                position=5
            ))
        ]
        self.assertEqual(self.plan1.skills.count(), 5)
        self.assertQuerysetEqual(self.plan1.skills.all(), expected)

        # Add the skill again to the next level, should only add one more
        # plan entry
        self.plan1.add_to_plan(skill, 3)
        self.assertEqual(self.plan1.skills.count(), 6)

        # Add a skill known to the character then try and add it to the plan
        # should result in no more planned skill
        skill = Skill.objects.get(name='Hull Upgrades')
        SkillTrained.objects.create(
            character=self.character1,
            skill=skill,
            level=1
        )
        self.plan1.add_to_plan(skill, 1)
        self.assertEqual(self.plan1.skills.count(), 6)
        self.assertFalse(self.plan1.skills.filter(
            skill__name='Hull Upgrades'
        ))
