from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from product_cellar_app.models import ProductCellar

size_options = [
    ["0-2", "0-2"],
    ["2-4", "2-4"],
    ["6-8", "6-8"],
    ["10-12", "10-12"],
    ["14-16", "14-16"],
    ["XS", "XS"],
    ["S", "S"],
    ["M", "M"],
    ["L", "L"],
    ["XL", "XL"],
    ["XXL", "XXL"],
    ["XXXL", "XXXL"],
]

color_options = [
    ["#faf38c", "AMARILLO"],
    ["#fc3b5a", "ROJO"],
    ["#082c56", "AZUL OSCURO"],
    ["#21637c", "AZUL VERDOSO"],
    ["#ffffff", "BLANCO"],
    ["#0b1518", "NEGRO"],
    ["#7D7D7D", "GRIS"],
    ["#7D7D7D", "LILA"],
    ["#f3eea4", "HUESO"]
]

state_options = [
    ["OK", "PRODUCTO OK"],
    ["DEFECTIVE", "PRODUCTO DEFECTUOSO"],
    ["DAMAGED", "PRODUCTO DAÑADO"]
]


class ClothingCellar(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    product_cellar = models.ForeignKey(ProductCellar, on_delete=models.PROTECT)
    size = models.CharField(default='NONE', max_length=20, choices=size_options)
    color = models.CharField(default='#7D7D7D', max_length=10, choices=color_options)
    state = models.CharField(default='OK', max_length=20, choices=state_options)
    info = models.TextField(default='OK')
