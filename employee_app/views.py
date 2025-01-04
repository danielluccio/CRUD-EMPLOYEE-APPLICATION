from django.shortcuts import render
from . import models
from .form import EmployeeForms


def employeeForm(request):
    form = EmployeeForms()
    return render(request, 'employeeForm.html', {'form': form})

def employeeList(request):
    pass

def employeeDelete(request):
    pass
