from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel
from person_app.models import Person


class Client(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)