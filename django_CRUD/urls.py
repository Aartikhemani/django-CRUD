"""django_CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from employee_registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.EmployeeFormView.as_view(), name='employee_form'),
    path('<int:id>/',views.EmployeeFormView.as_view(), name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('employee_list/', views.employee_list, name='employee_list'),
]
