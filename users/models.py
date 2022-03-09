from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _  # i think this is right, but need to test it
from django.utils.text import slugify


class MyUserManager(BaseUserManager):
	
	def create_user(self, email, username, password=None, **other_fields):
		if not email:
			raise ValueError(_('You must provide an email address.'))
		if not password:
			raise ValueError(_('You must provide a password.'))
		email = self.normalize_email(email)
		user = self.model(email=email, username=username, **other_fields)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self, email, username, password=None, **other_fields):
		other_fields.setdefault('is_active', True)
		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser', True)
		
		return self.create_user(email, username, password, **other_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True)
	username = models.CharField(max_length=32, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(blank=True, null=True)
	
	is_active = models.BooleanField(default=True)  # set default to False, then to True after confirming email
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	objects = MyUserManager()
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	
	def __str__(self):
		return self.username


class UserProfile(models.Model):
	user = models.OneToOneField(MyUser, related_name='profile', on_delete=models.CASCADE, null=True)
	
	first = models.CharField(max_length=64, null=True, blank=True)
	last = models.CharField(max_length=64, null=True, blank=True)
	phone = PhoneNumberField(null=True, blank=True)
	about = models.TextField(max_length=500, null=True, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)
	
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=50, null=True, blank=True)
	is_instructor = models.BooleanField(default=False)
	
	
	def save(self, *args, **kwargs):
		if not self.slug:
			slug = slugify(self.user.username)
			check = UserProfile.objects.filter(slug=slug)
			if check:
				while check:
					slug = f'{slug}-{UserProfile.objects.filter(slug__startswith=slug).count()}'
					check = UserProfile.objects.filter(slug=slug)
					continue
				self.slug = slug
			else:
				self.slug = slug
		super().save(*args, **kwargs)
	
	
	def __str__(self):
		return f'{self.first} {self.last}'


class ProfileSettings(models.Model):
	show_email = models.BooleanField(default=True)
	show_last = models.BooleanField(default=True)
	show_phone = models.BooleanField(default=False)
	show_about = models.BooleanField(default=True)
	show_location = models.BooleanField(default=True)
	
	settings = models.OneToOneField(UserProfile, related_name='settings', on_delete=models.CASCADE, null=True)
	

class Course(models.Model):
	name = models.CharField(max_length=64, default='COURSE')
	time = models.CharField(max_length=64, default='TIME')
	ages = models.CharField(max_length=64, default='Kids and Adults')
	cost = models.CharField(max_length=8, default='$')
	billing = models.CharField(max_length=16, choices=(('WEEK', 'WEEK'), ('MONTH', 'MONTH'), ('YEAR', 'YEAR'), ('ONCE', 'ONCE')), default='MONTH')
	description = models.CharField(max_length=255, default='DESCRIPT')
	
	instructor = models.ManyToManyField(UserProfile, related_name='instructor', limit_choices_to={'is_instructor': True})
	
	def __str__(self):
		return self.name


class ContactUs(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField(max_length=255)
	subject = models.CharField(max_length=255, null=True, blank=True)
	message = models.TextField(max_length=1000, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	resolved = models.BooleanField(default=False)
	
	class Meta:
		verbose_name_plural = 'Contact Us'
		
	def __str__(self):
		return self.name
	

class DirectMessageThread(models.Model):
	user = models.ForeignKey(UserProfile, related_name='+', on_delete=models.SET_NULL, null=True)
	receiver = models.ForeignKey(UserProfile, related_name='+', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.user.user.username
	

class DirectMessage(models.Model):
	thread = models.ForeignKey(DirectMessageThread, related_name='thread', on_delete=models.CASCADE, blank=True)
	
	sender = models.ForeignKey(UserProfile, related_name='sender', on_delete=models.SET_NULL, null=True)
	receiver = models.ForeignKey(UserProfile, related_name='receiver', on_delete=models.SET_NULL, null=True)
	
	message = models.TextField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.sender.user.username} {self.receiver.user.username}'
	

class ForumRoom(models.Model):
	host = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=1000, null=True, blank=True)
	participants = models.ManyToManyField(UserProfile, related_name='participants', blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-updated', '-created']
	
	def __str__(self):
		return self.title


class ForumMessage(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	room = models.ForeignKey(ForumRoom, on_delete=models.CASCADE)
	body = models.TextField(max_length=5000)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['updated', 'created']
	
	def __str__(self):
		return self.body
