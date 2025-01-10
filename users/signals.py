from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# sender- sends the signal
# instance- instance of the model that sent the signal or the user that was created
# created- boolean value that checks if the user was created or not
# kwargs- keyword arguments
# receiver- receives the signal and performs the action
# sender- the model that sends the signal
# it is fired after the user is saved, it creates a profile for the user, the profile is created with the user as the instance
@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    if created:
        # creates a profile for the user
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# ! in the app.py we add configuration for the signals
