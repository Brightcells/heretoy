from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Profile


class UserBackend(object):
    def authenticate(self, uid):
        try:
            user = Profile.objects.get(uid=uid)
        except ObjectDoesNotExist:
            return None
        return user.user

    def get_user(self, user_pk):
        try:
            return User.objects.get(pk=user_pk)
        except ObjectDoesNotExist:
            return None
