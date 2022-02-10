from django.contrib import admin
from django.urls import path, include
from users.views import HomeView, CourseListView, SignupView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('', HomeView.as_view(), name='index'),
	path('admin/', admin.site.urls),
	path('users/', include('users.urls', namespace='users')),
	path('courses/', CourseListView.as_view(), name='courses'),
	path('signup/', SignupView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
]
