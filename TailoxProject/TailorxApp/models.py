from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from PIL import Image


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


class Post(models.Model):
    """
    this is our database model
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
            'auth.User',
            on_delete=models.CASCADE,)
    body = models.TextField()


    def __str__(self):
        """return a string rep of a post instance"""
        return self.title


class Picture(models.Model):
    """
    A class representing pictures uploaded by tailors.
    """
    tailor = models.ForeignKey(Tailor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tailor_pictures')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to ensure the image size is within 2MB.
        """
        if self.image:
            max_size = 2 * 1024 * 1024  # 2MB
            if self.image.size > max_size:
                raise ValueError("Image size should be less than 2MB.")
        super(Picture, self).save(*args, **kwargs)


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
