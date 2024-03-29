from django.db import models  
from django.forms import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Tailor, Picture


class ClientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class TailorRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserImage(forms.Form):
    image = forms.ImageField()
    caption = forms.CharField(max_length=200)

    class meta:  
        # To specify the model to be used to create form  
        models = Picture 
        # It includes all the fields of model  
        fields = '__all__'
