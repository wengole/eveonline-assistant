from django.test import TestCase
from characters.models import Character, ApiKey
from users.models import User


class TestPlan(TestCase):
    fixtures = ['skills']

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(
            
        )
        cls.apikey = ApiKey.objects.create(
            key_id = '1234',
            verification_code='abc123',

        )
        cls.character = Character.objects.create(
            apikey=apikey,

        )