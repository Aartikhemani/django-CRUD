from django import forms

from employee_registration.models import EmployeeForm


class EmployeeFormForms(forms.ModelForm):
    class Meta:
        model = EmployeeForm
        fields = ["name",'em_code','mobile','position']