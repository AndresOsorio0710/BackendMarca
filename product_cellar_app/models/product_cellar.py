from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel
from cellar_app.models import Cellar
from provider_app.models import Provider


class ProductCellar(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    cellar = models.ForeignKey(Cellar, on_delete=models.PROTECT)  # bodega
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)  # proveedor
    reference = models.CharField(max_length=20, default='PROD-C-')
    name = models.CharField(max_length=50, default='NOT INCLUDED')  # nombre
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=8)  # costo
    unit_cost = models.DecimalField(default=0, decimal_places=2, max_digits=7)  # costo unitario
    quantity_entered = models.PositiveIntegerField(default=0)  # cantidad ingresada
    free_quantity = models.PositiveIntegerField(default=0)
    stop = models.PositiveIntegerField(default=0)  # cantidad minima permitida
    description = models.TextField(default='NOT INCLUDED')  # descripcion

    def __str__(self):
        cellar = Cellar.objects.get(uuid=self.cellar_id)
        provider = Provider.objects.get(uuid=self.provider_id)
        return (cellar.name + "-" + self.name + "-" + provider.name)
