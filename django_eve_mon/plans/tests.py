from django.test import TestCase
from characters.models import Character, ApiKey, SkillTrained
from plans.models import Plan, PlannedSkill
from skills.models import Skill
from users.models import User


class TestPlan(TestCase):
    fixtures = ['skills', 'users', 'characters',]

    def setUp(self):
        self.user = User.objects.get(username='test_user')
        self.character = Character.objects.get(name='TestChar')
        self.apikey = ApiKey.objects.get(key_id='1234')
        self.plan = Plan.objects.create(
            name='Test Plan',
            character=self.character,
            user=self.user
        )

    def test_setUp(self):
        self.assertIsNotNone(self.user)
        self.assertIsNotNone(self.character)
        self.assertIsNotNone(self.apikey)
        self.assertIsNotNone(self.plan)

    def test_add_to_plan(self):
        self.maxDiff = None

        # Add a skill with requirements to the plan and ensure the planned
        # skills are correct
        skill = Skill.objects.get(name='Armor Layering')
        self.plan.add_to_plan(
            skill=skill,
            level=2
        )
        expected = [
            repr(PlannedSkill(
                plan=self.plan,
                skill=Skill.objects.get(name='Mechanics'),
                level=1,
                position=1
            )),
            repr(PlannedSkill(
                plan=self.plan,
                skill=Skill.objects.get(name='Mechanics'),
                level=2,
                position=2
            )),
            repr(PlannedSkill(
                plan=self.plan,
                skill=Skill.objects.get(name='Mechanics'),
                level=3,
                position=3
            )),
            repr(PlannedSkill(
                plan=self.plan,
                skill=Skill.objects.get(name='Armor Layering'),
                level=1,
                position=4
            )),
            repr(PlannedSkill(
                plan=self.plan,
                skill=Skill.objects.get(name='Armor Layering'),
                level=2,
                position=5
            ))
        ]
        self.assertEqual(self.plan.skills.count(), 5)
        self.assertQuerysetEqual(self.plan.skills.all(), expected)

        # Add the skill again to the next level, should only add one more
        # plan entry
        self.plan.add_to_plan(skill, 3)
        self.assertEqual(self.plan.skills.count(), 6)

        # Add a skill known to the character then try and add it to the plan
        # should result in no more planned skill
        skill = Skill.objects.get(name='Hull Upgrades')
        SkillTrained.objects.create(
            character=self.character,
            skill=skill,
            level=1
        )
        self.plan.add_to_plan(skill, 1)
        self.assertEqual(self.plan.skills.count(), 6)
        self.assertFalse(self.plan.skills.filter(
            skill__name='Hull Upgrades'
        ))
