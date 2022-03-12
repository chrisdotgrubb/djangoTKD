import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser, UserProfile, ProfileSettings


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
	if created:
		logging.info(f'User "{instance.username}" created')


@receiver(post_save, sender=UserProfile)
def create_settings(sender, instance, created, **kwargs):
	if created:
		logging.info(f'Profile "{instance}" created')


@receiver(post_save, sender=ProfileSettings)
def create_settings(sender, instance, created, **kwargs):
	if created:
		logging.info(f'Settings "{instance}" created')

