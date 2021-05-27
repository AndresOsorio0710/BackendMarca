from django.contrib import admin
from .models import ProductCellar


class ProductCellarAdmin(admin.ModelAdmin):
    list_display = ["reference", "name", "cellar", "provider", "cost", "unit_cost", "free_quantity"]
    list_filter = ["cellar", "provider"]
    list_per_page = 10
    search_fields = ["reference", "name", "cost", "unit_cost", "free_quantity"]


admin.site.register(ProductCellar, ProductCellarAdmin)
