from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ["person"]
    list_per_page = 10


admin.site.register(Client, ClientAdmin)
