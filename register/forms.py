from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(forms.Form):
    user_name = forms.CharField(label='username',max_length=20)
    pass_word = forms.CharField(label='password',max_length=20)

    

    