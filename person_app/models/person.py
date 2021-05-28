from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models

id_type_options = [
    ["C.C.", "CEDULA DE CIUDADANIA"],
    ["C.E.", "CEDULA DE EXTRANJERIA"],
    ["N.I.P.", "NUMERO DE IDENTIFICACION PERSONAL"],
    ["N.I.T.", "NUMERO DE IDENTIFICACION TRIBUTARIA"],
    ["T.I.", "TARJETA DE IDENTIDAD"],
    ["P.A.P.", "PASAPORTE"]
]

gender_options = [
    ["M", "MASCULINO"],
    ["F", "FEMENINO"],
    ["I", "NO DEFINIDO"],
    ["N", "NO SUMINISTRADO"]
]


class Person(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    id_type = models.CharField(default='NOT INCLUDED', max_length=15, choices=id_type_options)
    id = models.CharField(default='NOT INCLUDED', max_length=20)
    name = models.CharField(max_length=80, default='NOT INCLUDED')
    last_name = models.CharField(max_length=80, default='NOT INCLUDED')
    address = models.CharField(max_length=80, default='NOT INCLUDED')
    phone_number = models.CharField(max_length=12, default='NOT INCLUDED')
    email = models.EmailField(default='notIncluded@marca.com')
    gender = models.CharField(default='I', max_length=1, choices=gender_options)

    def __str__(self):
        return (self.id + "-" + self.last_name + " " + self.name)
