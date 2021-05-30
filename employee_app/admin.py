from django.contrib import admin
from employee_app.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['person', 'job', 'salary', 'commission_pct']
    list_per_page = 10


admin.site.register(Employee, EmployeeAdmin)
