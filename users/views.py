from django.shortcuts import render
from django.views.generic import ( TemplateView, CreateView,
                    UpdateView, DeleteView, DetailView)
from .models import User
# Create your views here.

class HomeView(TemplateView):
    template_name = 'users/home.html'


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = 'users/user_create.html'
    success_url = '/users'

class ProfileView(DetailView):
    template_name = 'users/profile.html'
    model = User
    context_object_name = 'user'


class ProfileUpdateView(UpdateView):
    model = User
    fields = ['username','first_name', 'last_name', 'email', 'password', 'profile_picture']
    template_name = 'users/profile_update.html'
    success_url = 'users'


class ProfileDeleteView(DeleteView):
    model = User
    template_name = 'users/profile_delete.html'
    success_url = '/users'

