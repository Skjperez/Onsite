from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    user_name = forms.CharField(label='Username',max_length=20)
    pass_word = forms.CharField(label='Password',max_length=20)

    

    