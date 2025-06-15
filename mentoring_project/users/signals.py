from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Profile
from django.contrib.auth.signals import user_login_failed


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, request, **kwargs):

    username = credentials.get('username', None)
    if username:
        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            profile.last_failed_login = timezone.now()
            profile.save()
        except (User.DoesNotExist, Profile.DoesNotExist):
            pass