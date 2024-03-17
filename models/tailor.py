#!/usr/bin/python3

from django.db import models
from basemodel import BaseModel
from datetime import datetime


class Tailor(BaseModel):
    """
    A class representing a tailor user.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        """
        Override the save method to set created_at and updated_at.
        """
        if not self.id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super(Tailor, self).save(*args, **kwargs)


    @classmethod
    def create(cls, email, password, first_name=None, last_name=None):
        """
        Create a new Tailor instance and save it to the database.
        """
        new_tailor = cls(email=email, password=password, first_name=first_name, last_name=last_name)
        new_tailor.save()
        return new_tailor
