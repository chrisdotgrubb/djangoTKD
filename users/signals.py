import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser, UserProfile, ProfileSettings


@receiver(post_save, sender=MyUser)
def create_user(sender, instance, created, **kwargs):
	if created:
		logging.info(f'User "{instance}" created')


@receiver(post_save, sender=UserProfile)
def create_profile(sender, instance, created, **kwargs):
	if created:
		logging.info(f'Profile for "{type(instance)}" created')


@receiver(post_save, sender=ProfileSettings)
def create_settings(sender, instance, created, **kwargs):
	if created:
		logging.info(f'Settings for "{type(instance)}" created')
		