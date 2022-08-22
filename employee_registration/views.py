from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import *

from employee_registration.forms import EmployeeFormForms


class EmployeeFormView(View):
    def get(self,request, id=0):
        if id == 0:
            form = EmployeeFormForms()
        else:
            employee = EmployeeForm.objects.get(pk=id)
            form = EmployeeFormForms(instance=employee)
        return render(request, 'employee/employee_form.html',{'form':form})

    def post(self,request, id=0):
        if id == 0:
           form = EmployeeFormForms(request.POST)
        else:
            employee = EmployeeForm.objects.get(pk=id)
            form = EmployeeFormForms(request.POST,instance=employee)
        if form.is_valid():
            messages.success(request, "Registered Successfully")
            form.save()
        return redirect('/employee_list')


def employee_list(request):
    list = EmployeeForm.objects.all()
    return render(request, 'employee/employee_list.html',{'list':list})


def employee_delete(request,id):
    employee = EmployeeForm.objects.get(pk=id)
    employee.delete()
    return redirect('/employee_list')
