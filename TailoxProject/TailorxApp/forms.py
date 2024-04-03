from django.db import models  
from django.forms import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Tailor, Picture, State


class ClientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class TailorRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=100)
    business_name = forms.CharField(max_length=128)
    address = forms.CharField(max_length=255)
    location = forms.ModelChoiceField(queryset=State.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'business_name', 'address', 'location', 'password1', 'password2']


class UserImageForm(forms.Form):
    image = forms.ImageField(label="Portfolio Image")
    caption = forms.CharField(max_length=200)

    class meta:  
        # To specify the model to be used to create form  
        models = Picture 
        # It includes all the fields of model  
        fields = '__all__'
