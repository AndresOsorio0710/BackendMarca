from django.db.models import F, Sum, Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from clothing_cellar_app.models import ClothingCellar
from clothing_cellar_app.serializers import ClothingCellarSerializer, ListClothingProductCellarSerializer


class ClothingCellarViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ClothingCellar.objects.all()
    serializer_class = ClothingCellarSerializer

    def get_queryset(self):
        queryset = super(ClothingCellarViewSet, self).get_queryset()
        if self.action == self.get_cpc.__name__:
            queryset = queryset.values(
                'uuid',
                'product_cellar',
                'size',
                'color',
                'state',
                'info'
            ).annotate(
                name=F('product_cellar__name'),
                cellar=F('product_cellar__cellar__name'),
                provider=F('product_cellar__provider__name'),
                reference=F('product_cellar__reference')
            )
        return queryset

    def get_serializer_class(self):
        serializer = {
            'get_cpc': ListClothingProductCellarSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return ClothingCellarSerializer

    @action(methods=['GET'], detail=False, url_name='cpc', url_path='cpc', name='cpc')
    def get_cpc(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
