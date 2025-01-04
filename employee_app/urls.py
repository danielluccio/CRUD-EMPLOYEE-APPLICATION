from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeeForm, name='employeeForm'),
    path('employeeList/', views.employeeList, name='employeeList'),
    path('employeeDelete/', views.employeeDelete, name='employeeDelete'),
]