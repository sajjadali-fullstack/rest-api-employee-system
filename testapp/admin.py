from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'emp_id', 'first_name', 'last_name', 'department', 'designation', 'email', 'salary', 'joining_date']

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)