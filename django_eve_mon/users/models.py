from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def has_apikeys(self):
        """
        Does this user have an API Keys registered

        :return: :rtype: bool
        """
        return len(self.api_keys) > 0

    def __unicode__(self):
        return self.username