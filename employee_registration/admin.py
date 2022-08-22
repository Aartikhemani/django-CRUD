from django.contrib import admin

# Register your models here.
from employee_registration.models import EmployeeForm, Position

admin.site.register(Position)


@admin.register(EmployeeForm)
class EmployeeForm(admin.ModelAdmin):
    list_display = ['name','em_code','mobile','position']