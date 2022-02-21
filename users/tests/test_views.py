from django.test import TestCase, RequestFactory
from django.urls import reverse
from users.models import MyUser
from users.views import ProfileView


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
