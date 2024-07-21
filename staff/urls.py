from django.urls import path
from .views import StaffCreateView, StaffDetailView, StaffUpdateView, StaffListView

app_name = 'staff'

urlpatterns = [
    path('', StaffListView.as_view(), name='staff-list'),
    path('create/', StaffCreateView.as_view(), name='staff-create'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('<int:pk>/update/', StaffUpdateView.as_view(), name='staff-update'),
]