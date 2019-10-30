from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from allauth.compat import force_str, ugettext_lazy as _


class CustomProcessAdapter(DefaultAccountAdapter):
    # self.error_messages['email_taken'] = _("A user is already registered with this e-mail address.") 
    def clean_username(self, username):
        if len(username) > 8:
            raise ValidationError('Please enter a username value less than the current one')
        return DefaultAccountAdapter.clean_username(self,username) # For other default validations.

    def clean_email(self,email):
        RestrictedList = ['test@test.com']
        if email in RestrictedList:
            raise ValidationError('You are restricted from registering. Please contact admin.')
        return email

    def clean_password(self,password):
    	if len(password) > 20:
    		raise ValidationError('Please Enter a password greater that you can remember.')
    	return DefaultAccountAdapter.clean_password(self,password)

    def validate_unique_email(self, email):
        if email_address_exists(email):
            #raise forms.ValidationError(self.error_messages['email_taken'])
            raise forms.ValidationError('THIS IS A TEST')
        return email