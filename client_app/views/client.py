from django.db.models import F, Sum
from rest_framework import viewsets, mixins
from client_app.models import Client
from client_app.serializers import ClientSerializer


class ClientViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
