from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_unusable_password()
        instance.username = instance.email.split('@')[0]
        if commit:
            instance.save()
        return instance


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
