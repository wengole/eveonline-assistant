from braces.views import UserPassesTestMixin


class UserIsOwnerMixin(UserPassesTestMixin):

    def test_func(self, user):
        return self.get_object().is_owner(user)