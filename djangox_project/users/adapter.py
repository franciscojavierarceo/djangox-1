from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from allauth.compat import force_str, ugettext_lazy as _

class CustomProcessAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        RestrictedList = ['test@test.com']
        print('running validation...')
        if email in RestrictedList:
            raise ValidationError('You are restricted from registering. Please contact admin.')
        return email


def email_has_banned_domain(e):
    return "@test.com" in e

class MyAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        print('THIS IS A TEST OF CLEAN EMAIL')
        email = super().clean_email(email)
        if email_has_banned_domain(email):
            raise ValidationError("Your domain is bad.")
        return email

    def clean_username(self, username):
        print('THIS IS A TEST OF CLEAN USERNAME')
        if len(username) > 0:
            raise ValidationError('Please enter a username value less than the current one')
        return DefaultAccountAdapter.clean_username(self,username) # For other default validations.