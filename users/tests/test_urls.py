from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.test import TestCase
from django.urls import reverse, resolve

from users.views import HomeView, CourseListView, SignupView, FAQView, AboutView, OtherServicesView, ContactUsMessagesView, ForumView, ForumRoomCreateView, ForumRoomView, ProfileView, \
	ProfileUpdateView, UserProfileDetailView, UserProfileListView, ThreadView, ThreadListView


class TestUrls(TestCase):
	
	def setUp(self):
		pass
	
	def test_signup_url(self):
		url = '/signup/'
		rev_url = reverse('signup')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, SignupView)
	
	def test_login_url(self):
		url = '/login/'
		rev_url = reverse('login')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, LoginView)
	
	def test_logout_url(self):
		url = '/logout/'
		rev_url = reverse('logout')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, LogoutView)
	
	def test_password_reset_url(self):
		url = '/password-reset/'
		rev_url = reverse('password_reset')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, PasswordResetView)
	
	def test_password_rest_done_url(self):
		url = '/password-reset-done/'
		rev_url = reverse('password_reset_done')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, PasswordResetDoneView)
	
	def test_password_rest_confirm_url(self):
		url = '/password-reset-confirm/1/1/'
		rev_url = reverse('password_reset_confirm', args=[1, 1])
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, PasswordResetConfirmView)
	
	def test_password_rest_complete_url(self):
		url = '/password-reset-complete/'
		rev_url = reverse('password_reset_complete')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, PasswordResetCompleteView)
	
	def test_home_url(self):
		url = '/'
		rev_url = reverse('index')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, HomeView)
	
	def test_faq_url(self):
		url = '/faq/'
		rev_url = reverse('faq')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, FAQView)
	
	def test_about_url(self):
		url = '/about/'
		rev_url = reverse('about')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, AboutView)
	
	def test_other_services_url(self):
		url = '/other-services/'
		rev_url = reverse('other-services')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, OtherServicesView)
	
	def test_courses_url(self):
		url = '/courses/'
		rev_url = reverse('courses')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, CourseListView)
	
	def test_forum_url(self):
		url = '/forum/'
		rev_url = reverse('forum')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ForumView)
	
	def test_forum_room_create_url(self):
		url = '/forum/room/create/'
		rev_url = reverse('create-room')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ForumRoomCreateView)
	
	def test_forum_room_url(self):
		url = '/forum/room/1/'
		rev_url = reverse('room', args=[1])
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ForumRoomView)
	
	def test_contact_us_messages_url(self):
		url = '/contact-us-messages/'
		rev_url = reverse('contact-us-messages')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ContactUsMessagesView)
	
	def test_users_url(self):
		url = '/users/'
		rev_url = reverse('users:user-list')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, UserProfileListView)
	
	def test_profile_url(self):
		url = '/users/profile/'
		rev_url = reverse('users:profile')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ProfileView)
	
	def test_profile_edit_url(self):
		url = '/users/profile/edit/1/'
		rev_url = reverse('users:profile-edit', args=[1])
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ProfileUpdateView)
	
	def test_profile_detail_url(self):
		url = '/users/profile/1/'
		rev_url = reverse('users:user-profile', args=[1])
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, UserProfileDetailView)
	
	def test_inbox_url(self):
		url = '/users/inbox/'
		rev_url = reverse('users:inbox')
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ThreadListView)
	
	def test_thread_url(self):
		url = '/users/message/1/'
		rev_url = reverse('users:thread', args=[1])
		self.assertEqual(url, rev_url)
		self.assertEqual(resolve(url).func.view_class, ThreadView)
