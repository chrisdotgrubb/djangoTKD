from django.test import TestCase
from users.models import MyUser, UserProfile, Course, DirectMessageThread, ForumRoom, DirectMessage, ContactUs


class TestMyUser(TestCase):
	
	email = None
	username = None
	password = None
	
	@classmethod
	def setUpTestData(cls):
		cls.email = 'valid@test.com'
		cls.username = 'valid user'
		cls.password = 'password'
		
		cls.user = MyUser.objects.create_user(email=cls.email, username=cls.username, password=cls.password)
	
	def test_email(self):
		self.assertEqual(self.user.email, self.email)
	
	def test_username(self):
		self.assertEqual(self.user.username, self.username)
		
	def test_password(self):
		self.assertTrue(self.user.check_password(self.password))
		
	def test_str(self):
		self.assertEqual(str(self.user), self.username)

class TestUserProfile(TestCase):
	
	email = None
	username = None
	password = None
	first = None
	last = None
	phone = None
	about = None
	location = None
	profile = None
	
	@classmethod
	def setUpTestData(cls):
		cls.email = 'valid@test.com'
		cls.username = 'valid user'
		cls.password = 'password'
		cls.first = 'first name'
		cls.last = 'last name'
		cls.phone = '8145740000'
		cls.about = 'about me'
		cls.location = 'State College'
		
		cls.user = MyUser.objects.create_user(email=cls.email, username=cls.username, password=cls.password)
		cls.profile = MyUser.objects.get(username=cls.username).profile
		cls.profile.first = cls.first
		cls.profile.last = cls.last
		cls.profile.phone = cls.phone
		cls.profile.about = cls.about
		cls.profile.location = cls.location
	
	def test_first(self):
		self.assertEqual(self.profile.first, self.first)
		
	def test_last(self):
		self.assertEqual(self.profile.last, self.last)
		
	def test_phone(self):
		self.assertEqual(self.profile.phone, self.phone)
		
	def test_about(self):
		self.assertEqual(self.profile.about, self.about)
		
	def test_location(self):
		self.assertEqual(self.profile.location, self.location)
		
	def test_slug(self):
		self.assertEqual(self.profile.slug, 'valid-user')
		
	def test_str(self):
		self.assertEqual(str(self.profile), f'{self.first} {self.last}')
	

class TestCourse(TestCase):
	name = None
	time = None
	ages = None
	cost = None
	billing = None
	description = None
	
	@classmethod
	def setUpTestData(cls):
		cls.name = 'name'
		cls.time = 'time'
		cls.ages = 'ages'
		cls.cost = '$50'
		cls.billing = 'MONTHLY'
		cls.description = 'description'
		
		cls.course = Course.objects.create(
			name=cls.name,
			time=cls.time,
			ages=cls.ages,
			cost=cls.cost,
			billing=cls.billing,
			description=cls.description,
		)
		
	def test_name(self):
		self.assertEqual(self.course.name, self.name)
		
	def test_time(self):
		self.assertEqual(self.course.time, self.time)
		
	def test_ages(self):
		self.assertEqual(self.course.ages, self.ages)
		
	def test_cost(self):
		self.assertEqual(self.course.cost, self.cost)
		
	def test_billing(self):
		self.assertEqual(self.course.billing, self.billing)
		
	def test_description(self):
		self.assertEqual(self.course.description, self.description)
		
	def test_str(self):
		self.assertEqual(str(self.course), self.name)
		

class TestContactUs(TestCase):
	name = None
	email = None
	subject = None
	message = None
	# resolved = None
	
	@classmethod
	def setUpTestData(cls):
		cls.name = 'name'
		cls.email = 'email'
		cls.subject = 'subject'
		cls.message = 'message'
		# cls.resolved = True
		
		cls.contact = ContactUs.objects.create(name=cls.name, email=cls.email, subject=cls.subject, message=cls.message)
	
	def test_name(self):
		self.assertEqual(self.contact.name, self.name)
		
	def test_email(self):
		self.assertEqual(self.contact.email, self.email)
		
	def test_subject(self):
		self.assertEqual(self.contact.subject, self.subject)
		
	def test_message(self):
		self.assertEqual(self.contact.message, self.message)
		
	def test_resolved(self):
		self.assertEqual(self.contact.resolved, False)
		self.contact.resolved = True
		self.assertEqual(self.contact.resolved, True)
	
	def test_str(self):
		self.assertEqual(str(self.contact), self.name)
		

class TestDirectMessageThread(TestCase):
	user_1 = None
	user_2 = None
	receiver = None
	username = None
	
	@classmethod
	def setUpTestData(cls):
		cls.username = 'test user'
		cls.user_1 = MyUser.objects.create_user(email='a@a.com', username=cls.username, password='password')
		cls.user_2 = MyUser.objects.create_user(email='b@a.com', username='another', password='password')
		cls.thread = DirectMessageThread.objects.create(user=cls.user_1.profile, receiver=cls.user_2.profile)
		
	def test_user(self):
		self.assertEqual(self.thread.user, self.user_1.profile)
	
	def test_receiver(self):
		self.assertEqual(self.thread.receiver, self.user_2.profile)
		
	def test_str(self):
		self.assertEqual(str(self.thread), f'{self.user_1.username} to {self.user_2.username}')
		
	
	