from django.contrib import admin
from .models import ProductCellarSale


class ProductCellarSaleAdmin(admin.ModelAdmin):
    list_display = ['product_sale', 'product_cellar', 'quantity', 'cost']
    list_filter = ['product_sale']
    list_per_page = 10
    search_fields = ['product_sale', 'product_cellar']


admin.site.register(ProductCellarSale, ProductCellarSaleAdmin)
