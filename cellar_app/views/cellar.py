from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from cellar_app.models import Cellar
from cellar_app.serializers import CellarSerializer, SaveCellarSerializer, ListLiteCellarSerializer


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

        if self.action == self.get_lite.__name__:
            queryset = queryset.only('uuid', 'name')

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveCellarSerializer,
            'get_lite': ListLiteCellarSerializer
        }
        if self.action in serializer:
            return serializer[self.action]

        return CellarSerializer

    @action(methods=['GET'], detail=False, url_name='lite', url_path='lite', name='lite')
    def get_lite(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
