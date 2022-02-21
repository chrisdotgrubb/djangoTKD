from django.db.models import QuerySet
from django.test import TestCase, RequestFactory
from django.urls import reverse

from users.models import MyUser, Course, DirectMessageThread
from users.views import ProfileView, ProfileUpdateView, CourseListView, ThreadListView


class SignupTest(TestCase):
	
	def setUp(self):
		self.url = reverse('signup')
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_post(self):
		data = {'username': 'name', 'email': 'test@test.com', 'password1': 'G00Dpassword', 'password2': 'G00Dpassword'}
		response = self.client.post(self.url, data=data)
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('login'))
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'registration/signup.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class HomeTest(TestCase):
	
	def setUp(self):
		self.url = reverse('index')
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_post(self):
		data = {'name': 'test', 'email': 'a@test.com'}
		response = self.client.post(self.url, data=data)
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('index'))
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'index.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class FAQTest(TestCase):
	
	def setUp(self):
		self.url = reverse('faq')
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'faq.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class AboutTest(TestCase):
	
	def setUp(self):
		self.url = reverse('about')
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'about.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class OtherServicesTest(TestCase):
	
	def setUp(self):
		self.url = reverse('other-services')
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'other_services.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class UserProfileTest(TestCase):
	
	def setUp(self):
		self.url = reverse('users:user-list')
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'users/user_list.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class ProfileTest(TestCase):
	
	def setUp(self):
		self.url = reverse('users:profile')
		self.client.force_login(MyUser.objects.get_or_create(username='test')[0])
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
		self.client.logout()
		self.response = self.client.get(self.url)
		self.assertEqual(self.response.status_code, 302)
	
	def test_queryset(self):  # not usual qs, is just 'self.request.user'
		request = RequestFactory().get(self.url)
		request.user = self.client  # needed since request has no attribute 'user'
		view = ProfileView()
		view.request = request
		queryset = view.get_queryset()
		self.assertEqual(queryset, self.client)  #
		# self.assertQuerysetEqual(queryset, self.client)  	# instead use this to eval 2 querysets, but self.client isn't a qs
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'users/profile.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class UserProfileUpdateTest(TestCase):
	
	def setUp(self):
		self.user = MyUser.objects.create_user('test@test.com', 'user', 'G00Dpassword')
		self.user.profile.slug = 'slug'
		self.url = reverse('users:profile-edit', args=[self.user.profile.slug])
		self.client.force_login(self.user)
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
		self.client.logout()
		self.response = self.client.get(self.url)
		self.assertEqual(self.response.status_code, 302)
	
	def test_post(self):
		data = {'first': 'first', 'last': 'last', 'phone': '(814)574-1111', 'about': 'about', 'location': 'location'}
		response = self.client.post(self.url, data=data)
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('users:profile'))
		
	def test_queryset(self):
		request = RequestFactory().get(self.url)
		request.user = self.user
		view = ProfileUpdateView()
		view.request = request
		queryset = view.get_queryset()
		self.assertQuerysetEqual(queryset, [self.user.profile])
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'users/profile_edit.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class UserProfileDetailTest(TestCase):
	
	def setUp(self):
		self.user = MyUser.objects.create_user('test@test.com', 'user', 'G00Dpassword')
		self.user.profile.slug = 'slug'
		self.url = reverse('users:user-profile', args=[self.user.profile.slug])
		self.client.force_login(self.user)
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
		self.client.logout()
		self.response = self.client.get(self.url)
		self.assertEqual(self.response.status_code, 302)
		
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'users/user_profile.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class CourseListTest(TestCase):
	
	def setUp(self):
		self.url = reverse('courses')
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_queryset(self):
		request = RequestFactory().get(self.url)
		view = CourseListView()
		view.request = request
		queryset = view.get_queryset()
		self.assertQuerysetEqual(queryset, [])
		
		course_1 = Course.objects.create(
			name='Course 1',
			time='time',
			ages='ages',
			cost='$50',
			billing='MONTHLY',
			description='description'
		)
		
		request = RequestFactory().get(self.url)
		view = CourseListView()
		view.request = request
		queryset = view.get_queryset()
		self.assertQuerysetEqual(queryset, ['<Course: Course 1>'])
		
		course_2 = Course.objects.create(
			name='Course 2',
			time='time',
			ages='ages',
			cost='$50',
			billing='WEEKLY',
			description='description'
		)
		
		course_3 = Course.objects.create(
			name='Course 3',
			time='time',
			ages='ages',
			cost='$50',
			billing='ONCE',
			description='description'
		)
		
		request = RequestFactory().get(self.url)
		view = CourseListView()
		view.request = request
		queryset = view.get_queryset()
		self.assertEqual(len(queryset), 3)
		
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'users/course_list.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')
	
class ContactUsMessagesTest(TestCase):
	
	def setUp(self):
		self.user = MyUser.objects.create_user('is_su@test.com', 'super', 'G00Dpassword', is_superuser=True)
		self.url = reverse('contact-us-messages')
		self.client.force_login(self.user)
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
		self.user.is_superuser = False
		self.user.save()
		self.response = self.client.get(self.url)
		self.assertEqual(self.response.status_code, 403)
		self.client.logout()
		self.response = self.client.get(self.url)
		self.assertEqual(self.response.status_code, 302)
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'contact_us_messages.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class ThreadListTest(TestCase):
	
	def setUp(self):
		self.user1 = MyUser.objects.create_user('test1@test.com', 'user 1', 'G00Dpassword')
		self.url = reverse('users:inbox')
		self.client.force_login(self.user1)
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
		self.client.logout()
		self.response = self.client.get(self.url)
		self.assertEqual(self.response.status_code, 302)
	
	def test_queryset(self):
		request = RequestFactory().get(self.url)
		request.user = self.user1
		view = ThreadListView()
		view.request = request
		queryset = view.get_queryset(request=view.request)
		self.assertIsInstance(queryset, QuerySet)
		self.assertEqual(len(queryset), 0)
		
		user_2 = MyUser.objects.create_user('test2@test.com', 'user 2', 'G00Dpassword')
		user_3 = MyUser.objects.create_user('test3@test.com', 'user 3', 'G00Dpassword')
		
		thread_1 = DirectMessageThread.objects.create(user=self.user1.profile, receiver=user_2.profile)
		thread_2 = DirectMessageThread.objects.create(user=user_2.profile, receiver=self.user1.profile)
		thread_3 = DirectMessageThread.objects.create(user=user_2.profile, receiver=user_3.profile)
		queryset = view.get_queryset(request=view.request)
		self.assertIsInstance(queryset, QuerySet)
		self.assertEqual(len(queryset), 2)
		
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'users/inbox.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')


class ThreadTest(TestCase):
	
	def setUp(self):
		self.user_1 = MyUser.objects.create_user('test1@test.com', 'user 1', 'G00Dpassword')
		self.user_2 = MyUser.objects.create_user('test2@test.com', 'user 2', 'G00Dpassword')
		self.thread = DirectMessageThread.objects.create(user=self.user_1.profile, receiver=self.user_2.profile)
		self.client.force_login(self.user_1)
		self.url = reverse('users:thread', args=[self.user_2.profile.slug])
		self.response = self.client.get(self.url)
	
	def test_get(self):
		self.assertEqual(self.response.status_code, 200)
		self.client.logout()
		self.response = self.client.get(self.url)
		self.assertEqual(self.response.status_code, 302)
	
	def test_post(self):
		pass
	
	# def test_queryset(self):
	# 	request = RequestFactory().get(self.url)
	# 	request.user = self.user
	# 	view = ThreadListView()
	# 	view.request = request
	# 	queryset = view.get_queryset(request=view.request)
	# 	self.assertIsInstance(queryset, QuerySet)
	# 	self.assertEqual(len(queryset), 0)
	#
	# 	user_2 = MyUser.objects.create_user('test2@test.com', 'user 2', 'G00Dpassword')
	# 	user_3 = MyUser.objects.create_user('test3@test.com', 'user 3', 'G00Dpassword')
	#
	# 	thread_1 = DirectMessageThread.objects.create(user=self.user.profile, receiver=user_2.profile)
	# 	thread_2 = DirectMessageThread.objects.create(user=user_2.profile, receiver=self.user.profile)
	# 	thread_3 = DirectMessageThread.objects.create(user=user_2.profile, receiver=user_3.profile)
	# 	queryset = view.get_queryset(request=view.request)
	# 	self.assertIsInstance(queryset, QuerySet)
	# 	self.assertEqual(len(queryset), 2)
	
	def test_template_index(self):
		self.assertTemplateUsed(self.response, 'users/thread.html')
	
	def test_template_navbar(self):
		self.assertTemplateUsed(self.response, 'navbar.html')
	
	def test_template_footer(self):
		self.assertTemplateUsed(self.response, 'footer.html')
		
		