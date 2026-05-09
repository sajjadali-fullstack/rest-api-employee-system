from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'first_name', 'last_name', 'department', 'designation', 'joining_date']

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)