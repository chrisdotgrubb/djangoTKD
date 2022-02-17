from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.models import inlineformset_factory
from .models import MyUser, UserProfile, ContactUs, DirectMessage, DirectMessageThread, ForumRoom, ForumMessage


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = MyUser
		fields = ('username', 'email', 'password1', 'password2')
		field_classes = {'username': UsernameField, }


class CustomUserUpdateForm(UserCreationForm):
	class Meta:
		model = MyUser
		fields = ('username', 'email')
		field_classes = {'username': UsernameField, }


class UserProfileModelForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
			'first',
			'last',
			'phone',
			'about',
			'location',
		)


class UserProfileUpdateModelForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
			'first',
			'last',
			'phone',
			'about',
			'location',
		)


class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = (
			'name',
			'email',
			'subject',
			'message',
		)


class DirectMessageThreadForm(forms.Form):
	message = forms.CharField(label='message', max_length=1000)


class DirectMessageForm(forms.ModelForm):
	class Meta:
		model = DirectMessage
		fields = (
			'message',
		)


class ForumRoomForm(forms.ModelForm):
	class Meta:
		model = ForumRoom
		fields = (
			'title',
			'description',
		)


class ForumMessageForm(forms.ModelForm):
	class Meta:
		model = ForumMessage
		fields = (
			'body',
		)
