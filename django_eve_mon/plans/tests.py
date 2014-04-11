from django.test import TestCase
from skills.models import Skill


class TestPlan(TestCase):
    @classmethod
    def setUpClass(cls):
        skill_1 = Skill(

        )