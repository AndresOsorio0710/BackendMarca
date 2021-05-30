from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel
from person_app.models import Person
from job_app.models import Job


class Employee(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    salary = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    commission_pct = models.IntegerField(default=0)

    def __str__(self):
        return self.person
