from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .form import EmployeeForms
from .models import Employee


def employeeForm(request, id=0):
    if request.method == 'GET':
        if id == 0:  # Criação de um novo registro
            form = EmployeeForms()
        else:  # Edição de um registro existente
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForms(instance=employee)
        return render(request, 'employeeForm.html', {'form': form})
    
    else:  # Método POST
        if id == 0:  # Criação
            form = EmployeeForms(request.POST)
        else:  # Edição
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForms(request.POST, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect("/employee/employeeList/")
        
        # Caso os dados não sejam válidos, retornar o formulário com erros
        return render(request, 'employeeForm.html', {'form': form})

def employeeList(request):
    employeeList = Employee.objects.all()
    context = {'employeeList': employeeList}
    return render(request, 'employeeList.html', context)

def employeeDelete(request, id):
    employee = Employee.objects.get(pk=id)
    if employee.delete():
        return redirect('/employee/employeeList/')
