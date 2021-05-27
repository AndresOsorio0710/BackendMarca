from django.db.models import F, Sum
from rest_framework import viewsets, mixins
from product_cellar_app.models import ProductCellar
from product_cellar_app.serializers import ProductCellarSerializer, SaveProductCellarSerializer, \
    ListProductSerializer


class ProductCellarViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductCellar.objects.all()
    serializer_class = ProductCellarSerializer

    def get_queryset(self):
        queryset = super(ProductCellarViewSet, self).get_queryset()

        if self.action == self.list.__name__:
            queryset = queryset.values(
                'uuid',
                'name',
                'reference',
                'description',
                'cost',
                'unit_cost',
                'quantity_entered',
                'free_quantity',
                'stop',
            ).annotate(
                cellarName=F('cellar__name'),
                cellar=F('cellar'),
                providerName=F('provider__name'),
                provider=F('provider')
            ).order_by('name')

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductCellarSerializer,
            'list': ListProductSerializer
        }

        if self.action in serializer:
            return serializer[self.action]

        return ProductCellarSerializer
