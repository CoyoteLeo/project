from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['email'].required = False

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class PasswordForgetForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
