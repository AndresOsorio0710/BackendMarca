from django.contrib import admin
from .models import ProductSale


class ProductSaleAdmin(admin.ModelAdmin):
    list_display = ["name", "reference", "section", "collection", "cost", "price", "utility", "discount",
                    "discount_unit"]
    search_fields = ["name", "section", "collection"]
    list_filter = ["section", "collection", "discount"]
    list_per_page = 5


admin.site.register(ProductSale, ProductSaleAdmin)
