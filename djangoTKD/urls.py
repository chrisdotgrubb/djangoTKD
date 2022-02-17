from django.contrib import admin
from django.urls import path, include
from users.views import HomeView, CourseListView, SignupView, FAQView, AboutView, OtherServicesView, ContactUsMessagesView, ForumView, ForumRoomCreateView, ForumRoomView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
	path('', HomeView.as_view(), name='index'),
	path('admin/', admin.site.urls),
	path('faq/', FAQView.as_view(), name='faq'),
	path('about/', AboutView.as_view(), name='about'),
	path('other-services/', OtherServicesView.as_view(), name='other-services'),
	path('users/', include('users.urls', namespace='users')),
	path('courses/', CourseListView.as_view(), name='courses'),
	path('forum/', ForumView.as_view(), name='forum'),
	path('forum/room/create', ForumRoomCreateView.as_view, name='create-room'),
	path('forum/room/<int:pk>', ForumRoomView.as_view(), name='room'),
	path('contact-us-messages/', ContactUsMessagesView.as_view(), name='contact-us-messages'),
	path('signup/', SignupView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('reset-password', PasswordResetView.as_view(), name='reset-password'),
	path('password-reset-done', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
