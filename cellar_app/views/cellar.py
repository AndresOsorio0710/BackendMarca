from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from cellar_app.models import Cellar
from cellar_app.serializers import CellarSerializer, SaveCellarSerializer, ListCellarSerializer


class CellarViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Cellar.objects.all()
    serializer_class = CellarSerializer

    def get_queryset(self):
        queryset = super(CellarViewSet, self).get_queryset()

        if self.action == self.get_short.__name__:
            queryset = queryset.only('uuid', 'short_name', 'name', 'free_capacity')

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveCellarSerializer,
            'get_short': ListCellarSerializer
        }
        if self.action in serializer:
            return serializer[self.action]

        return CellarSerializer

    @action(methods=['GET'], detail=False, url_name='short', url_path='short', name='short')
    def get_short(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
