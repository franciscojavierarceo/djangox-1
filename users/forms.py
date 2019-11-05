from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from django.forms import ValidationError
from allauth.account.adapter import get_adapter

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
    email = forms.EmailField(
        label='Email Address', 
        widget=forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                    }
            )
    )
    class Meta:
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_unusable_password()
        instance.username = get_username(instance.email)
        instance.email = self.cleaned_data.get('email')
        print("")
        print("*********SAVE METHOD RUNNING*************")
        print("")

        if commit:
            instance.save()

        return instance

    def email_has_banned_domain(self, e):
        return "@test." in e.lower()

    def clean_email(self):
        email = self.cleaned_data['email']
        if self.email_has_banned_domain(email):
            raise ValidationError("Email has banned domain")
        return email

    def validate_email(self, email):
        print("VALIDTE METHOD RUNNING")
        email = get_adapter().clean_email(email)
        return email

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
