from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views import generic
from .models import UserProfile, Course, MyUser, ContactUs
from .forms import UserProfileModelForm, CustomUserCreationForm, CustomUserUpdateForm, UserProfileUpdateModelForm, ContactUsForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignupView(generic.CreateView):
	template_name = 'registration/signup.html'
	form_class = CustomUserCreationForm
	
	def get_success_url(self):
		return reverse('login')


class HomeView(generic.CreateView):
	template_name = 'index.html'
	form_class = ContactUsForm
	
	def get_success_url(self):
		return reverse('index')


class FAQView(generic.TemplateView):
	template_name = 'faq.html'


class AboutView(generic.TemplateView):
	template_name = 'about.html'


class OtherServicesView(generic.TemplateView):
	template_name = 'other_services.html'


class UserProfileListView(generic.ListView):
	template_name = 'users/user_list.html'
	queryset = UserProfile.objects.all()
	context_object_name = 'profiles'


class ProfileView(LoginRequiredMixin, generic.ListView):
	template_name = 'users/profile.html'
	
	def get_queryset(self):
		user = self.request.user
		return user


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
	template_name = 'users/profile_edit.html'
	form_class = UserProfileUpdateModelForm
	
	def get_queryset(self):
		user = self.request.user
		queryset = UserProfile.objects.filter(user=user)
		return queryset
	
	def get_success_url(self):
		return reverse('users:profile')


class UserProfileDetailView(generic.DetailView):
	template_name = 'users/user_profile.html'
	model = UserProfile

# def get_context_data(self, **kwargs):
# 	context = super().get_context_data(**kwargs)
# 	return context


class CourseListView(generic.ListView):
	template_name = 'users/course_list.html'
	queryset = Course.objects.all()
	context_object_name = 'courses'

class ContactUsMessagesView(UserPassesTestMixin, generic.ListView):
	template_name = 'contact_us_messages.html'
	queryset = ContactUs.objects.all()
	
	def test_func(self):
		return self.request.user.is_superuser
