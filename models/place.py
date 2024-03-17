#!/usr/bin/python3
"""a city model"""
from django.db import models
from basemodel import BaseModel
from city import City


class Place(BaseModel):
    """
    A class representing a place within a city.
    """
    name = models.CharField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='places')
    description = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the Place instance.
        """
        return f"{self.name}, {self.city}"
