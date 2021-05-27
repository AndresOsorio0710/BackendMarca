from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel


class Collection(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=50, default='NOT INCLUDED')
    icon = models.CharField(max_length=50, default='far fa-boxes')
    description = models.TextField(default='NOT INCLUDED')

    def __str__(self):
        return self.name
