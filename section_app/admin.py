from django.contrib import admin
from .models import Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'description']
    list_editable = ['icon', 'description']
    search_fields = ['name', 'description']
    list_per_page = 5


admin.site.register(Section, SectionAdmin)
