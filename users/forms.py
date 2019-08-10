from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model
#from allauth.account.forms import SignupForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.utils.translation import gettext_lazy as _

def get_username(email, splitter="@"):
    try:
        emailparts = email.split(splitter)
        user = emailparts[0]
        domain = ''.join(emailparts[1:]).replace(".", "_")
        username = "{user}_{domain}".format(**{
                "user": user,
                "domain": domain,
            }
        )
        return username
    except:
        return None

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', )

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        user.set_unusable_password()
        return user

class CustomUserCreationForm2(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_unusable_password()
        instance.username = self.clean_username(get_username(instance.email))
        if commit:
            instance.save()
        return instance


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
