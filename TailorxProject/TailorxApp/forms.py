from django.db import models  
from django.forms import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Tailor, Picture, State, Profile


class ClientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    address = forms.CharField()

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'address', 'password1', 'password2']

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


# Create a UserUpdateForm to update a username and email
class TailorUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    skills = forms.CharField(max_length=1024)
    experience = forms.IntegerField()
    certifications = forms.CharField()
    phone_number = forms.CharField()

    class Meta:
        model = Profile
        fields = ['image', 'skills', 'experience', 'certifications', 'phone_number'] 


class PictureImageForm(forms.ModelForm):
    caption = forms.CharField(max_length=200)

    class Meta:    
        model = Picture   
        fields = ['image', 'caption']
