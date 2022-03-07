from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import MyUser, UserProfile, ContactUs, DirectMessage, ForumRoom, ForumMessage, ProfileSettings


class CustomUserCreationForm(UserCreationForm):
	password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
	password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}))
	
	class Meta:
		model = MyUser
		fields = ('username', 'email', 'password1', 'password2')
		field_classes = {'username': UsernameField, }
		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'Enter a username'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
		}


class CustomUserUpdateForm(UserCreationForm):
	class Meta:
		model = MyUser
		fields = ('username', 'email')
		field_classes = {'username': UsernameField,}


class UserProfileUpdateModelForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
			'first',
			'last',
			'phone',
			'location',
			'about',
		)
		widgets = {
			'first': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
			'last': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
			'phone':  forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
			'location': forms.TextInput(attrs={'placeholder': 'Enter your city/state'}),
			'about':  forms.Textarea(attrs={'placeholder': 'Enter something about yourself'}),
		}


class ProfileSettingsModelForm(forms.ModelForm):
	class Meta:
		model = ProfileSettings
		exclude = ('settings',)
		widgets = {
			'show_email': forms.CheckboxInput(attrs={'title': 'Checking this box makes your email show on your public profile page'}),
			'show_last': forms.CheckboxInput(attrs={'title': 'Checking this box makes your last name show on your public profile page'}),
			'show_phone': forms.CheckboxInput(attrs={'title': 'Checking this box makes your phone number show on your public profile page'}),
			'show_location': forms.CheckboxInput(attrs={'title': 'Checking this box makes your location show on your public profile page'}),
			'show_about': forms.CheckboxInput(attrs={'title': 'Checking this box makes your about-me show on your public profile page'}),
		}


class ProfileEditMultiForm(MultiModelForm):
	form_classes = {
		'profile': UserProfileUpdateModelForm,
		'settings': ProfileSettingsModelForm,
	}


class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = (
			'name',
			'email',
			'subject',
			'message',
		)
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
			'subject': forms.TextInput(attrs={'placeholder': 'Enter the subject'}),
			'message': forms.Textarea(attrs={'placeholder': 'Type your message here'}),
		}


class DirectMessageForm(forms.ModelForm):
	class Meta:
		model = DirectMessage
		fields = (
			'message',
		)
		widgets = {'message': forms.Textarea(attrs={'placeholder': 'Enter a message, then click Send.'})}


class ForumRoomForm(forms.ModelForm):
	class Meta:
		model = ForumRoom
		fields = (
			'title',
			'description',
		)
		widgets = {
			'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
			'description': forms.Textarea(attrs={'placeholder': 'Enter a description'})
		}


class ForumMessageForm(forms.ModelForm):
	class Meta:
		model = ForumMessage
		fields = (
			'body',
		)
		widgets = {'body': forms.Textarea(attrs={'placeholder': 'Enter a message, then click Post.'})}
