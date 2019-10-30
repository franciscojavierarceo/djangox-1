from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

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

        if commit:
            instance.save()

        return instance

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
