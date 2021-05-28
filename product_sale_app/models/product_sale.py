from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel
from section_app.models import Section
from collection_app.models import Collection


class ProductSale(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    reference = models.CharField(max_length=20, default='CELL-PROD-###-####')
    name = models.CharField(max_length=50, default='NOT INCLUDED')
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    utility = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    discount = models.IntegerField(default=0)
    discount_unit = models.IntegerField(default=0)
    description = models.TextField(default='NOT INCLUDED')

    def __str__(self):
        return (self.reference + " " + self.name)
