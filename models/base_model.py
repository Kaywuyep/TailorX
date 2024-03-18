#!/usr/bin/python3
"""a base model for our tailorx project"""

from django.db import models
import uuid
from datetime import datetime


class BaseModel(models.Model):
    """A base model for Django models providing common attributes and methods.
    it inherits from the models.Model, the base class for all django models
    Attributes:
        id (str): A universally unique identifier (UUID) for d model instance
        created_at (datetime): The timestamp indicating when
                               the instance was created.
        updated_at (datetime): The timestamp indicating when
                               the instance was last updated.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    
    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the updated_at attribute before saving.
        """
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing all keys/values of the instance's attributes,
                  along with the class name and timestamps in ISO 8601 format.
        """
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
            **self.__dict__,
        }

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation containing the class name, id, and attribute dictionary.
        """
        return f"[{self.__class__.__name__}] ({self.id})"
