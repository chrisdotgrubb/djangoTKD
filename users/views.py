from django.db.models import Q
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import generic
from .models import UserProfile, Course, MyUser, ContactUs, DirectMessageThread, DirectMessage, ForumRoom, ForumMessage
from .forms import CustomUserCreationForm, UserProfileUpdateModelForm, ContactUsForm, DirectMessageForm, ForumRoomForm, ForumMessageForm
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
	
	def get(self, request, *args, **kwargs):
		threads = DirectMessageThread.objects.filter(Q(user=request.user.profile) | Q(receiver=request.user.profile))
		
		context = {
			'threads': threads,
		}
		
		return render(request, 'users/inbox.html', context)


class ThreadView(LoginRequiredMixin, generic.View):
	
	def get(self, request, slug, *args, **kwargs):
		form = DirectMessageForm()
		receiver = UserProfile.objects.filter(slug=slug)[0]
		thread = DirectMessageThread.objects.filter(user=request.user.profile, receiver=receiver).first() or DirectMessageThread.objects.filter(user=receiver, receiver=request.user.profile).first()
		if thread:
			messages = DirectMessage.objects.filter(thread=thread)
			context = {
				'form': form,
				'thread': thread,
				'messages': messages,
			}
			
			return render(request, 'users/thread.html', context)
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
		
		if form.is_valid():
			new_message = DirectMessage(
				thread=thread,
				sender=request.user.profile,
				receiver=receiver,
				message=message,
			)
			new_message.save()
			return redirect('users:thread', slug)
		
		return render(request, 'users/thread.html')


class ForumView(LoginRequiredMixin, generic.ListView):
	template_name = 'users/forum.html'
	context_object_name = 'rooms'
	
	def get_queryset(self):
		return ForumRoom.objects.all()
	
	def get_context_data(self, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['my_rooms'] = ForumRoom.objects.filter(participants__user=self.request.user)
		return context


class ForumRoomCreateView(LoginRequiredMixin, generic.CreateView):
	template_name = 'users/forum_room_create.html'
	form_class = ForumRoomForm
	
	def get_initial(self):
		initial = super(ForumRoomCreateView, self).get_initial()
		initial['title'] = 'Enter A Title'
		initial['description'] = 'Enter A Description'
		return initial
	
	def form_valid(self, form):
		room = form.save(commit=False)
		room.host = self.request.user.profile
		room = form.save()
		room.participants.add(self.request.user.profile.id)
		room.save()
		self.kwargs['pk'] = room.id
		print(room.id)
		print(self.kwargs['pk'])
		return super(ForumRoomCreateView, self).form_valid(form)
	
	def get_success_url(self):
		print(self.kwargs['pk'])
		return reverse('room', kwargs={'pk':self.kwargs['pk']})


class ForumRoomView(LoginRequiredMixin, generic.View):
	
	def get(self, request, pk, *args, **kwargs):
		form = ForumMessageForm()
		room = ForumRoom.objects.filter(id=pk).first()
		messages = ForumMessage.objects.filter(room_id=pk)
		if room:
			context = {
				'form': form,
				'room': room,
				'messages': messages,
			}
			return render(request, 'users/room.html', context)
		
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
			
			return redirect('room', pk=room.id)
	
