from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def has_apikeys(self):
        """
        Does this user have an API Keys registered

        :return: :rtype: bool
        """
        return self.api_keys.count() > 0

    def has_disabled_characters(self):
        """
        Does this user have characters that aren't yet added

        :return: :rtype: bool
        """
        return self.characters.filter(enabled=False).count() > 0

    def __unicode__(self):
        return self.username