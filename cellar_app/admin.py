from django.contrib import admin
from .models import Cellar


class CellarAdmin(admin.ModelAdmin):
    list_display = ["name", "short_name", "max_capacity", "free_capacity", "email", "phone_number", "address"]
    search_fields = ["name", "short_name", "max_capacity", "free_capacity", "email", "phone_number", "address",
                     "description"]
    list_filter = ["name"]
    list_per_page = 5


admin.site.register(Cellar, CellarAdmin)
