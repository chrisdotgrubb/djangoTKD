from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import reverse, redirect
from django.template.response import TemplateResponse
from django.views import generic
from .models import UserProfile, Course, ContactUs, DirectMessageThread, DirectMessage, ForumRoom, ForumMessage
from .forms import CustomUserCreationForm, ContactUsForm, DirectMessageForm, ForumRoomForm, ForumMessageForm, ProfileEditMultiForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignupView(generic.CreateView):
	template_name = 'registration/signup.html'
	form_class = CustomUserCreationForm
	
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Account created, please log in.')
		return reverse('login')


class HomeView(generic.CreateView):
	template_name = 'index.html'
	form_class = ContactUsForm
	
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Thank you for contacting us.')
		return reverse('index') + '#'


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
	form_class = ProfileEditMultiForm
	
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update(instance={
			'profile': self.object,
			'settings': self.object.settings,
		})
		return kwargs
	
	def get_queryset(self):
		user = self.request.user
		queryset = UserProfile.objects.filter(user=user)
		return queryset
	
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Updated successfully.')
		return reverse('users:profile')


class UserProfileDetailView(LoginRequiredMixin, generic.DetailView):
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
	
	def get_queryset(self, request):
		return DirectMessageThread.objects.filter(Q(user=request.user.profile) | Q(receiver=request.user.profile))
	
	def get(self, request, *args, **kwargs):
		threads = self.get_queryset(request=request)
		
		context = {
			'threads': threads,
		}
		
		return TemplateResponse(request, 'users/inbox.html', context)


class ThreadView(LoginRequiredMixin, generic.View):
	
	def get(self, request, slug, *args, **kwargs):
		form = DirectMessageForm()
		receiver = UserProfile.objects.filter(slug=slug)[0]
		thread = DirectMessageThread.objects.filter(user=request.user.profile, receiver=receiver).first() or DirectMessageThread.objects.filter(user=receiver, receiver=request.user.profile).first()
		if thread:
			direct_messages = DirectMessage.objects.filter(thread=thread)
			context = {
				'form': form,
				'thread': thread,
				'direct_messages': direct_messages,
			}
			
			return TemplateResponse(request, 'users/thread.html', context)
		else:
			thread = DirectMessageThread(
				user=request.user.profile,
				receiver=receiver,
			)
			thread.save()
			return redirect('users:thread', slug)
	
	def post(self, request, slug, *args, **kwargs):
		form = DirectMessageForm(request.POST)
		message = request.POST.get('message')
		receiver = UserProfile.objects.filter(slug=slug)[0]
		thread = DirectMessageThread.objects.filter(user=request.user.profile, receiver=receiver).first() or DirectMessageThread.objects.filter(user=receiver, receiver=request.user.profile).first()
		
		if form.is_valid() and message:
			new_message = DirectMessage(
				thread=thread,
				sender=request.user.profile,
				receiver=receiver,
				message=message,
			)
			new_message.save()
			messages.add_message(self.request, messages.INFO, 'Message sent successfully.')
			return redirect('users:thread', slug)
		
		return TemplateResponse(request, 'users/thread.html')


class ForumView(LoginRequiredMixin, generic.ListView):
	template_name = 'users/forum.html'
	context_object_name = 'rooms'
	
	def get_queryset(self):
		return ForumRoom.objects.all()
	
	def get_context_data(self, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['my_rooms'] = ForumRoom.objects.filter(participants__user=self.request.user)
		return context


class ForumRoomCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
	template_name = 'users/forum_room_create.html'
	form_class = ForumRoomForm
	success_message = 'Successfully created a room'
	
	def form_valid(self, form):
		room = form.save(commit=False)
		room.host = self.request.user.profile
		room = form.save()
		room.participants.add(self.request.user.profile.id)
		room.save()
		self.kwargs['pk'] = room.id
		return super(ForumRoomCreateView, self).form_valid(form)
	
	def get_success_url(self):
		return reverse('room', kwargs={'pk': self.kwargs['pk']})


class ForumRoomView(LoginRequiredMixin, generic.View):
	
	def get(self, request, pk, *args, **kwargs):
		form = ForumMessageForm()
		room = ForumRoom.objects.filter(id=pk).first()
		comments = ForumMessage.objects.filter(room_id=pk)
		if room:
			context = {
				'form': form,
				'room': room,
				'comments': comments,
			}
			return TemplateResponse(request, 'users/room.html', context)
		
		else:
			return redirect('forum')
	
	def post(self, request, pk, *args, **kwargs):
		form = ForumMessageForm(request.POST)
		room = ForumRoom.objects.filter(id=pk).first()
		body = request.POST.get('body')
		room.participants.add(self.request.user.profile.id)
		
		if form.is_valid():
			new_message = ForumMessage(
				user=self.request.user.profile,
				room=room,
				body=body,
			)
			new_message.save()
			messages.add_message(request, messages.INFO, 'Comment posted successfully.')
			return redirect('room', pk=room.id)


def check_username(request):
	username = request.POST.get('username')
	if username:
		if get_user_model().objects.filter(username=username).exists():
			return HttpResponse('<div id="username-error" style="color:red">Username taken</div>')
		else:
			return HttpResponse('<div id="username-error" style="color:green">Username available</div>')
	else:
		return HttpResponse('<div id="username-error">&nbsp;</div>')


def check_email(request):
	email = request.POST.get('email')
	if email:
		if get_user_model().objects.filter(email=email).exists():
			return HttpResponse('<div id="email-error" style="color:red">Email taken</div>')
		else:
			return HttpResponse('<div id="email-error" style="color:green">Email available</div>')
	else:
		return HttpResponse('<div id="email-error">&nbsp;</div>')
	
	