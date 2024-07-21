from django.shortcuts import render
from users.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView )
# Create your views here.

class StaffListView(ListView):
    queryset = User.objects.filter(is_staff=True)
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff_list'


class StaffDetailView(DetailView):
    model = User
    template_name = 'staff/staff_detail.html'
    context_object_name = 'staff'


class StaffCreateView(CreateView):
    model = User
    template_name = 'staff/staff_create.html'


class StaffUpdateView(UpdateView):
    model = User
    fields = ['username','first_name', 'last_name', 'email','profile_picture']
    template_name = 'staff/staff_update.html'
    success_url = 'staff/'
