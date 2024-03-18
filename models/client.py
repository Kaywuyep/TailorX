#!/usr/bin/python3
"""a Client class that inherits from basemodel"""

from django.db import models
from django.contrib.auth.models import User
from .basemodel import BaseModel


class Client(BaseModel):
    """
    A class representing a client user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        """
        Override the save method to ensure strict user authentication.
        """
        if not self.id:
            # Create a new user instance if it doesn't exist
            user = User.objects.create_user(username=self.user.username, email=self.user.email)
            user.set_password(self.user.password)
            user.save()
            self.user = user
        super().save(*args, **kwargs)


    def __str__(self):
        """
        Returns a string representation of the Client instance.
        """
        return f"[Client] ({self.user.username}) {self.user.email}"
