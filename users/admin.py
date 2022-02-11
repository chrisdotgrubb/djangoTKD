from django.shortcuts import reverse
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, UserProfile, Course
from django.utils.safestring import mark_safe

User = get_user_model()


class InLineUserProfile(admin.StackedInline):
	model = UserProfile


class UserAdminConfig(UserAdmin):
	inlines = [InLineUserProfile]
	search_fields = ('email', 'username')
	list_filter = ('is_active', 'is_staff', 'is_superuser')
	ordering = ('-created',)
	list_display = ('username', 'email', 'created', 'last_login', 'is_active', 'is_staff', 'is_superuser')
	
	fieldsets = (
		(None, {'fields': ('username', 'password', 'email')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}))


class UserProfileAdminConfig(admin.ModelAdmin):
	search_fields = ('first', 'last', 'phone', 'location')
	list_filter = ('is_instructor',)
	ordering = ('-updated',)
	list_display = ('first', 'last', 'user_link', 'phone', 'location', 'updated', 'get_is_active')  # , 'user_link', 'get_is_active'
	
	fieldsets = (
		(None, {'fields': ('user', 'first', 'last', 'phone', 'location', 'about', 'slug')}),
		('Permissions', {'fields': ('is_instructor',)}))
	readonly_fields = ('slug',)
	
	def get_username(self, obj):
		return obj.user.username
	
	def get_is_active(self, obj):
		return obj.user.is_active
	
	def user_link(self, obj):
		url = reverse('admin:users_myuser_change', args=[obj.user.pk])
		link = f'<a href="{url}">{obj.user.username}</a>'
		return mark_safe(link)
	
	get_username.short_description = 'username'
	get_is_active.short_description = 'is active'
	user_link.short_description = 'username'


class CourseAdminConfig(admin.ModelAdmin):
	search_fields = ('name', 'time', 'ages', 'instructor__first')
	list_display = ('name', 'time', 'ages', 'cost', 'billing', 'get_instructors')
	ordering = ('name',)
	list_filter = ('cost', 'billing', 'instructor__last')
	filter_horizontal = ('instructor',)
	
	def get_instructors(self, obj):
		return ", ".join([i.first for i in obj.instructor.all()])  # not really recommended because of all the extra queries, but should work since db is small


admin.site.register(User, UserAdminConfig)
admin.site.register(UserProfile, UserProfileAdminConfig)
admin.site.register(Course, CourseAdminConfig)
