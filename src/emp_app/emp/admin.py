from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'staff_id', 'name', 'designation', 'department', 'salary'
        ]

admin.site.register(Employee, EmployeeAdmin)