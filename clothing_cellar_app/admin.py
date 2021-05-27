from django.contrib import admin
from clothing_cellar_app.models import ClothingCellar


class ClothingCellarAdmin(admin.ModelAdmin):
    list_display = ["product_cellar", "size", "color", "state"]
    search_fields = ["product_cellar", "size", "color", "state"]
    list_filter = ["product_cellar", "size", "color", "state"]
    list_per_page = 10


admin.site.register(ClothingCellar, ClothingCellarAdmin)
