import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser, UserProfile, ProfileSettings


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
	if created:
		logging.info(f'User "{instance.username}" created')
		UserProfile.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


@receiver(post_save, sender=UserProfile)
def create_settings(sender, instance, created, **kwargs):
	if created:
		ProfileSettings.objects.create(settings=instance)
		
		