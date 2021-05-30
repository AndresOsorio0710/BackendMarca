from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel


class Job(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=80, default='NOT INCLUDED')
    min_salary = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    max_salary = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title
