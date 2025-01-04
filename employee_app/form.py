from django import forms
from .models import Employee

class EmployeeForms(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'full_name': 'FullName',
            'emp_code': 'EMP.CODE',
        }