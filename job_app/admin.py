from django.contrib import admin
from job_app.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'min_salary', 'max_salary']
    list_filter = ['title']
    list_per_page = 10
    search_fields = ['title']


admin.site.register(Job, JobAdmin)
