from django.db.models import F, Sum, Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from clothing_cellar_app.models import ClothingCellar
from clothing_cellar_app.serializers import ClothingCellarSerializer, ListClothingCellarSerializer, \
    SaveClothingCellarSerializer, ListClothingProductCellarSerializer, ListClothingCellarGroupColorSerializer, \
    ListClothingCellarGroupSizeSerializer


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
    lookup_field = 'uuid'

    def get_queryset(self):
        queryset = super(ClothingCellarViewSet, self).get_queryset()
        if self.action == self.get_short.__name__:
            queryset = queryset.values('uuid', 'product_cellar', 'size', 'color', 'state', 'info')
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
        if self.action == self.get_group_size.__name__:
            queryset = queryset.filter(product_cellar=self.kwargs.get('uuid')).values('size').annotate(
                free=Count('size'))
        if self.action == self.get_group_color.__name__:
            queryset = queryset.filter(product_cellar=self.kwargs.get('uuid')).values('size','color').annotate(
                free=Count('color'))
        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveClothingCellarSerializer,
            'get_short': ListClothingCellarSerializer,
            'get_cpc': ListClothingProductCellarSerializer,
            'get_group_size': ListClothingCellarGroupSizeSerializer,
            'get_group_color': ListClothingCellarGroupColorSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return ClothingCellarSerializer

    @action(methods=['GET'], detail=False, url_name='cpc', url_path='cpc', name='cpc')
    def get_cpc(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_name='short', url_path='short', name='short')
    def get_short(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_name='size', url_path='size', name='size')
    def get_group_size(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_name='color', url_path='color', name='color')
    def get_group_color(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
