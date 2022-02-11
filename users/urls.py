from django.urls import path
from .views import UserProfileListView, ProfileView, ProfileUpdateView, UserProfileDetailView

app_name = 'users'

urlpatterns = [
	path('', UserProfileListView.as_view(), name='user-list'),
	path('profile/', ProfileView.as_view(), name='profile'),
	path('profile/edit/<slug:slug>', ProfileUpdateView.as_view(), name='profile-edit'),
	path('profile/<slug:slug>', UserProfileDetailView.as_view(), name='user-profile'),
]
