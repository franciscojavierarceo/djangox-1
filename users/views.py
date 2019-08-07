from allauth.account.views import SignupView

from users.forms import CustomUserCreationForm


class MySignupView(SignupView):
    form_class = CustomUserCreationForm
