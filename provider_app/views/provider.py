from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from provider_app.models import Provider
from rest_framework.response import Response
from provider_app.serializers import ProviderSerializer, ListLiteProviderSerializer


class ProviderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def get_queryset(self):
        queryset = super(ProviderViewSet, self).get_queryset()
        if self.action == self.get_lite.__name__:
            queryset = queryset.only('uuid', 'name')
        return queryset

    def get_serializer_class(self):
        serializer = {
            'get_lite': ListLiteProviderSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return ProviderSerializer

    @action(methods=['GET'], detail=False, url_name='lite', url_path='lite', name='lite')
    def get_lite(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
