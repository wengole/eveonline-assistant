from django.test import TestCase
from characters.models import ApiKey, Character
from plans.models import Plan
from users.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            'test_user',
            'test@user.com',
            '123'
        )
        self.user2 = User.objects.create_user(
            'test_user2',
            'test2@user.com',
            '123'
        )
        self.apikey1 = ApiKey.objects.create(
            key_id='1234',
            verification_code='abc123',
            user=self.user1
        )
        self.apikey2 = ApiKey.objects.create(
            key_id='5678',
            verification_code='abc123',
            user=self.user2
        )
        self.character1 = Character(
            1,
            apikey=self.apikey1,
            user=self.user1,
            name='TestChar',
            skillpoints='9'
        )
        self.character1.save()
        self.character2 = Character(
            2,
            apikey=self.apikey2,
            user=self.user2,
            name='TestChar2',
            skillpoints='9001'
        )
        self.character2.save()
        self.plan1 = Plan.objects.create(
            name='Test Plan',
            character=self.character1,
            user=self.user1
        )
        self.plan2 = Plan.objects.create(
            name='Test Plan2',
            character=self.character2,
            user=self.user2
        )
