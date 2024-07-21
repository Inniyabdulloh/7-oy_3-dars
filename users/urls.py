from django.urls import path
from .views import HomeView, UserCreateView, ProfileView, ProfileUpdateView, ProfileDeleteView

app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', UserCreateView.as_view(), name='profile-create'),
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('edit/<int:pk>/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile-delete'),
]