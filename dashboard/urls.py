from django.urls import path
from .views import owner_dashboard, staff_dashboard

urlpatterns = [
    path('', owner_dashboard, name='owner_dashboard'),
    path('staff/', staff_dashboard, name='staff_dashboard'),
]
