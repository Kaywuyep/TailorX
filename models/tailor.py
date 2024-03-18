#!/usr/bin/python3

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .basemodel import BaseModel
from datetime import datetime


class Tailor(BaseModel):
    """
    A class representing a tailor user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @classmethod
    def create(cls, email, password, first_name=None, last_name=None):
        """
        Create a new Tailor instance and save it to the database.
        """
        user = User.objects.create_user(username=email, email=email, password=password)

        # Create the tailor instance
        new_tailor = cls(user=user, first_name=first_name, last_name=last_name)
        new_tailor.save()
        return new_tailor

    def __str__(self):
        """
        Returns a string representation of the Tailor instance.
        """
        return f"[Tailor] ({self.user.username}) {self.user.email}"
