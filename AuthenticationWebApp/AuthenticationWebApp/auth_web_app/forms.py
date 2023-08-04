from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
      SignForm is custom form hwo can extend,
      UserCreationForm inherits BaseUserCreationForm,
      this class Meta is inheritance from BaseUserCreationForm
    """
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
        field_classes = {"username": UsernameField}


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()