from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models


class Provider(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    identification_type = models.CharField(max_length=7, default='NOT')
    identification = models.CharField(max_length=15, default='NOT INCLUDED')
    name = models.CharField(max_length=100, default='NOT INCLUDED')
    address = models.CharField(max_length=80, default='NOT INCLUDED')
    phone_number = models.CharField(max_length=12, default='NOT INCLUDED')
    email = models.EmailField(default='notIncluded@marca.com')
    description = models.TextField(default='NOT INCLUDED')

    def __str__(self):
        return self.name
