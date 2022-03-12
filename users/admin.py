import logging

from django.utils.translation import ngettext
from django.contrib.admin import RelatedOnlyFieldListFilter, EmptyFieldListFilter
from django.shortcuts import reverse
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Course, DirectMessage, DirectMessageThread, ContactUs, ForumRoom, ForumMessage, ProfileSettings
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.utils.safestring import mark_safe

User = get_user_model()


class InLineUserProfile(admin.StackedInline):
	model = UserProfile
	readonly_fields = ('slug',)


class InLineProfileSettings(admin.StackedInline):
	model = ProfileSettings
	
	
class UserAdminConfig(UserAdmin):
	form = CustomUserUpdateForm
	add_form = CustomUserCreationForm
	add_fieldsets = ((None, {'fields':('username', 'email', 'password1', 'password2')}),('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser')}))
	# inlines = [InLineUserProfile]
	search_fields = ('email', 'username')
	list_filter = ('is_active', 'is_staff', 'is_superuser', ('last_login', EmptyFieldListFilter))
	ordering = ('-created',)
	list_display = ('username', 'email', 'created', 'last_login', 'is_active', 'is_staff', 'is_superuser')
	
	actions = ['make_staff', 'make_not_staff', 'make_superuser', 'make_not_superuser']
	
	fieldsets = (
		(None, {'fields': ('username', 'password', 'email')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}))
	
	def make_staff(self, request, queryset):
		updated = queryset.update(is_staff=True)
		self.message_user(request, ngettext(
			'%d user was successfully marked as staff.',
			'%d users were successfully marked as staff.',
			updated,
		) % updated, messages.SUCCESS)
	
	def make_not_staff(self, request, queryset):
		updated = queryset.update(is_staff=False)
		self.message_user(request, ngettext(
			'%d user was successfully marked as not staff.',
			'%d users were successfully marked as not staff.',
			updated,
		) % updated, messages.SUCCESS)
	
	def make_superuser(self, request, queryset):
		queryset.update(is_staff=True)
		updated = queryset.update(is_superuser=True)
		self.message_user(request, ngettext(
			'%d user was successfully marked as superuser(and staff).',
			'%d users were successfully marked as superusers(and staff).',
			updated,
		) % updated, messages.SUCCESS)
	
	def make_not_superuser(self, request, queryset):
		updated = queryset.update(is_superuser=False)
		self.message_user(request, ngettext(
			'%d user was successfully marked as not superuser.',
			'%d users were successfully marked as not superusers.',
			updated,
		) % updated, messages.SUCCESS)


class UserProfileAdminConfig(admin.ModelAdmin):
	inlines = [InLineProfileSettings]
	search_fields = ('first', 'last', 'phone', 'location')
	list_filter = ('is_instructor', ('phone', EmptyFieldListFilter))
	ordering = ('-updated',)
	list_display = ('first', 'last', 'user_link', 'phone', 'location', 'updated', 'is_instructor', 'get_is_active')  # , 'user_link', 'get_is_active'
	
	fieldsets = (
		(None, {'fields': ('user', 'first', 'last', 'phone', 'location', 'about', 'slug')}),
		('Permissions', {'fields': ('is_instructor',)}))
	readonly_fields = ('slug',)
	
	actions = ['make_instructor', 'make_not_instructor', 'make_active', 'make_not_active']
	
	def make_instructor(self, request, queryset):
		updated = queryset.update(is_instructor=True)
		self.message_user(request, ngettext(
			'%d user was successfully marked as an instructor.',
			'%d users were successfully marked as instructors.',
			updated,
		) % updated, messages.SUCCESS)
	
	def make_not_instructor(self, request, queryset):
		updated = queryset.update(is_instructor=False)
		self.message_user(request, ngettext(
			'%d user was successfully marked as not an instructor.',
			'%d users were successfully marked as not instructors.',
			updated,
		) % updated, messages.SUCCESS)
	
	def make_active(self, request, queryset):
		updated = queryset.update(is_active=True)
		self.message_user(request, ngettext(
			'%d user was successfully marked as active.',
			'%d users were successfully marked as active.',
			updated,
		) % updated, messages.SUCCESS)
	
	def make_not_active(self, request, queryset):
		updated = queryset.update(is_active=False)
		self.message_user(request, ngettext(
			'%d user was successfully marked as inactive.',
			'%d users were successfully marked as inactive.',
			updated,
		) % updated, messages.SUCCESS)
	
	def get_username(self, obj):
		return obj.user.username
	
	def get_is_active(self, obj):
		return obj.user.is_active
	
	def user_link(self, obj):
		url = reverse('admin:users_myuser_change', args=[obj.user.pk])
		link = f'<a href="{url}">{obj.user.username}</a>'
		return mark_safe(link)
	
	make_instructor.short_description = 'Make instructor'
	get_username.short_description = 'username'
	get_is_active.short_description = 'is active'
	user_link.short_description = 'username'


class CourseAdminConfig(admin.ModelAdmin):
	search_fields = ('name', 'time', 'ages', 'instructor__first')
	list_display = ('name', 'time', 'ages', 'cost', 'billing', 'get_instructors')
	ordering = ('name',)
	list_filter = ('cost', 'billing', ('instructor', RelatedOnlyFieldListFilter))
	filter_horizontal = ('instructor',)
	
	# noinspection PyMethodMayBeStatic
	def get_instructors(self, obj):
		return ", ".join([i.last for i in obj.instructor.all()])  # not really recommended because of all the extra queries, but should work since db is small


class ContactUsConfig(admin.ModelAdmin):
	search_fields = ('name', 'email', 'subject', 'message', 'created')
	list_display = ('name', 'email', 'subject', 'message', 'created', 'resolved')
	list_filter = ('resolved',)
	actions = ['make_resolved', 'make_not_resolved']
	fields = ('name', 'email', 'subject', 'message', 'created', 'resolved')
	readonly_fields = ('name', 'email', 'subject', 'message', 'created')
	ordering = ('-created',)
	
	def make_resolved(self, request, queryset):
		updated = queryset.update(resolved=True)
		self.message_user(request, ngettext(
			'%d message was successfully marked as resolved.',
			'%d messages were successfully marked as resolved.',
			updated,
		) % updated, messages.SUCCESS)
	
	def make_not_resolved(self, request, queryset):
		updated = queryset.update(resolved=False)
		self.message_user(request, ngettext(
			'%d message was successfully marked as unresolved.',
			'%d messages were successfully marked as unresolved.',
			updated,
		) % updated, messages.SUCCESS)


class DirectMessageThreadConfig(admin.ModelAdmin):
	list_display = ('user', 'receiver')


class DirectMessageConfig(admin.ModelAdmin):
	list_display = ('sender', 'receiver', 'message', 'created', 'is_read')


class ForumRoomConfig(admin.ModelAdmin):
	list_display = ('host', 'title', 'description', 'created', 'get_participants')
	
	# noinspection PyMethodMayBeStatic
	def get_participants(self, obj):
		return ", ".join([i.user.username for i in obj.participants.all()])


class ForumMessageConfig(admin.ModelAdmin):
	list_display = ('user', 'room', 'body', 'created')


admin.site.register(User, UserAdminConfig)
admin.site.register(UserProfile, UserProfileAdminConfig)
admin.site.register(Course, CourseAdminConfig)
admin.site.register(DirectMessageThread, DirectMessageThreadConfig)
admin.site.register(DirectMessage, DirectMessageConfig)
admin.site.register(ContactUs, ContactUsConfig)
admin.site.register(ForumRoom, ForumRoomConfig)
admin.site.register(ForumMessage, ForumMessageConfig)
