from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models


class Cellar(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    short_name = models.CharField(max_length=6, default='CELLAR', null=True)
    name = models.CharField(max_length=50, default='NOT INCLUDED')
    max_capacity = models.PositiveIntegerField(default=0)
    free_capacity = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=80, default='NOT INCLUDED')
    phone_number = models.CharField(max_length=10, default='NOT INCLUDED')
    email = models.EmailField(default='notIncluded@marca.com')
    description = models.TextField(default='NOT INCLUDED')

    def __str__(self):
        return (self.short_name + " - " + self.name)
