from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
from django.contrib.auth import login
def get_socila_accounts(user):
    return SocialAccount.objects.filter(user=user)
def passwd_validate(request,user,passwd1,passwd2):
        if passwd1 == passwd2:
            user.set_password(passwd1)
            user.save()
            return True
        else:
            return False
