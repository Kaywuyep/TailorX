#!/usr/bin/python3
"""a city model"""
from django.db import models
from basemodel import BaseModel
from state import State


class City(BaseModel):
    """
    A class representing a local government area within a state.
    """
    name = models.CharField(max_length=100)
    state = models.ForeignKey('State', on_delete=models.CASCADE, related_name='cities')


    def __str__(self):
        """
        Returns a string representation of the City instance.
        """
        return f"{self.name}, {self.state}"
