from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    name = forms.CharField(max_length=101)
    surname = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'name', 'surname', 'email', 'password1', 'password2']
