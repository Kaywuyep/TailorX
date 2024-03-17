#!/usr/bin/python3

from django.db import models
from tailor import Tailor
from PIL import Image

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
