from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id_type', 'id', 'last_name', 'name', 'address', 'phone_number', 'email', 'gender']
    list_filter = ['id_type', 'gender']
    list_per_page = 10
    search_fields = ['id_type', 'id', 'last_name', 'name', 'address', 'phone_number', 'email', 'gender']


admin.site.register(Person, PersonAdmin)
