from django.db.models import Q
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import generic
from .models import UserProfile, Course, MyUser, ContactUs, DirectMessageThread, DirectMessage
from .forms import UserProfileModelForm, CustomUserCreationForm, CustomUserUpdateForm, UserProfileUpdateModelForm, ContactUsForm, DirectMessageThreadForm, DirectMessageForm
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
	
	
class ThreadListView(LoginRequiredMixin, generic.View):
	
	def get(self, request, *args, **kwargs):
		threads = DirectMessageThread.objects.filter(Q(user=request.user.profile) | Q(receiver=request.user.profile))
		
		context = {
			'threads': threads,
		}
		
		return render(request, 'users/inbox.html', context)
	

class ThreadCreateView(LoginRequiredMixin, generic.View):
	
	def get(self, request, *args, **kwargs):
		form = DirectMessageThreadForm()
		
		context = {
			'form': form,
		}
		
		return render(request, 'users/create_thread.html', context)
	
	def post(self, request, *args, **kwargs):
		form = DirectMessageThreadForm(request.POST)
		
		username = request.POST.get('username')
		print(username)
		try:
			receiver = UserProfile.objects.get(user__username=username)
			print(request.user)
			# print(DirectMessageThread.objects.filter(user__user__username=receiver, receiver=request.user))
			if DirectMessageThread.objects.filter(user__user__username=request.user, receiver=receiver).exists():
				thread = DirectMessageThread.objects.filter(user__user__username=request.user, receiver=receiver)[0]
				return redirect('thread', pk=thread.pk)
			# elif DirectMessageThread.objects.filter(user__user__username=receiver, receiver=request.user).exists():
			# 	thread = DirectMessageThread.objects.filter(user__user__username=receiver, receiver=request.user)[0]
			# 	return redirect('thread', pk=thread.pk)
			print(request.user)
			if form.is_valid():
				thread = DirectMessageThread(
					user=request.user.profile,
					receiver=receiver.user.profile,
				)
				thread.save()
				return redirect('thread', pk=thread.pk)
		except:
			return redirect('users:create-thread')


class ThreadView(LoginRequiredMixin, generic.View):
	
	def get(self, request, pk, *args, **kwargs):
		form = DirectMessageForm()
		thread = DirectMessageThread.objects.get(pk=pk)
		message_list = DirectMessage.objects.filter(thread__pk__contains=pk)
		context = {
			'thread': thread,
			'form': form,
			'message_list': message_list,
		}
		
		return render(request, 'users/thread.html', context)
	
	
	