from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from product_cellar_app.models import ProductCellar
from product_sale_app.models import ProductSale


class ProductCellarSale(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    product_cellar = models.ForeignKey(ProductCellar, on_delete=models.PROTECT)
    product_sale = models.ForeignKey(ProductSale, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=8, null=True)

    def __str__(self):
        product_cellar = ProductCellar.objects.get(uuid=self.product_cellar)
        product_sale = ProductSale.objects.get(uuid=self.product_sale)
        answer = product_sale.name, " - ", product_cellar.name
        return answer
