from django.contrib import admin
from django.urls import path, include
from users.views import HomeView, CourseListView, SignupView, FAQView, AboutView, OtherServicesView, ContactUsMessagesView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('', HomeView.as_view(), name='index'),
	path('admin/', admin.site.urls),
	path('faq/', FAQView.as_view(), name='faq'),
	path('about/', AboutView.as_view(), name='about'),
	path('other-services/', OtherServicesView.as_view(), name='other-services'),
	path('users/', include('users.urls', namespace='users')),
	path('courses/', CourseListView.as_view(), name='courses'),
	path('contact-us-messages/', ContactUsMessagesView.as_view(), name='contact-us-messages'),
	path('signup/', SignupView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
]
