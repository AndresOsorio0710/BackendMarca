from django.contrib import admin
from .models import Provider


class ProviderAdmin(admin.ModelAdmin):
    list_display = ["identification_type", "identification", "name", "email", "phone_number", "address"]
    search_fields = ["identification_type", "identification", "name", "email", "phone_number", "address", "description"]
    list_filter = ["identification_type"]
    list_per_page = 5


admin.site.register(Provider, ProviderAdmin)
