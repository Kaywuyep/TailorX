#!/usr/bin/python3
"""a Client class that inherits from basemodel"""

from django.db import models
from basemodel import BaseModel


class Client(BaseModel):
    """
    A class representing a client user.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        """
        Returns a string representation of the Client instance.
        """
        return f"[Client] ({self.id}) {self.email}"


    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the updated_at attribute before saving.
        """
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)
