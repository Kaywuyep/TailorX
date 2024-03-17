#!/usr/bin/python3
"""a state model"""
from django.db import models
from basemodel import BaseModel

class State(BaseModel):
    """
    A class representing a state in Nigeria.
    """
    name = models.CharField(max_length=28)


    def __str__(self):
        """
        Returns a string representation of the State instance.
        """
        return self.name
