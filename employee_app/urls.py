from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeeForm, name='employeeForm'),
    path('employeeList/', views.employeeList, name='employeeList'),
    path('<int:id>/', views.employeeForm, name='employeeUpdate'),
    path('employeeDelete/<int:id>', views.employeeDelete, name='employeeDelete'),
]