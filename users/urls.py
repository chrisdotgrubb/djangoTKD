from django.urls import path
from .views import UserProfileListView, ProfileView, ProfileUpdateView, UserProfileDetailView, ThreadCreateView, ThreadView, ThreadListView

app_name = 'users'

urlpatterns = [
	path('', UserProfileListView.as_view(), name='user-list'),
	path('profile/', ProfileView.as_view(), name='profile'),
	path('profile/edit/<slug:slug>/', ProfileUpdateView.as_view(), name='profile-edit'),
	path('profile/<slug:slug>/', UserProfileDetailView.as_view(), name='user-profile'),
	path('inbox/', ThreadListView.as_view(), name='inbox'),
	path('message/<slug:slug>/', ThreadView.as_view(), name='thread'),
	path('message/<slug:slug>/create', ThreadCreateView.as_view(), name='create-thread'),
]
