from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import Profile, Picture


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_picture(sender, instance, created, **kwargs):
    if created:
        Picture.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_picture(sender, instance, **kwargs):
    pictures = instance.pictures.all()
    for picture in pictures:
        picture.save()
