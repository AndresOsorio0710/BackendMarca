from rest_framework import viewsets, mixins
from product_cellar_sale_app.models import ProductCellarSale
from product_cellar_sale_app.serializer import ProductCellarSaleSerializer, SaveProductCellarSaleSerializer, \
    ListProductCellarSaleSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F


class ProductCellarSaleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = ProductCellarSale.objects.all()
    serializer_class = ProductCellarSaleSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        queryset = super(ProductCellarSaleViewSet, self).get_queryset()
        if self.action == self.get_list.__name__:
            queryset = queryset.values('uuid', 'quantity', 'cost', 'product_sale', 'product_cellar').annotate(
                product_sale_name=F('product_sale__name'), product_sale_price=F('product_sale__price'),
                product_cellar_name=F('product_cellar__name'), product_cellar_cost=F('product_cellar__cost'),
                product_cellar_quantity=F('product_cellar__free_quantity'))
        if self.action == self.get_list_ps.__name__:
            queryset = queryset.filter(product_sale=self.kwargs.get('uuid')).values('uuid', 'quantity', 'cost',
                                                                                    'product_sale',
                                                                                    'product_cellar').annotate(
                product_sale_name=F('product_sale__name'), product_sale_price=F('product_sale__price'),
                product_cellar_name=F('product_cellar__name'), product_cellar_cost=F('product_cellar__cost'),
                product_cellar_quantity=F('product_cellar__free_quantity'))
        if self.action == self.get_list_pc.__name__:
            queryset = queryset.filter(product_cellar=self.kwargs.get('uuid')).values('uuid', 'quantity', 'cost',
                                                                                      'product_sale',
                                                                                      'product_cellar').annotate(
                product_sale_name=F('product_sale__name'), product_sale_price=F('product_sale__price'),
                product_cellar_name=F('product_cellar__name'), product_cellar_cost=F('product_cellar__cost'),
                product_cellar_quantity=F('product_cellar__free_quantity'))
        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductCellarSaleSerializer,
            'get_list': ListProductCellarSaleSerializer,
            'get_list_ps': ListProductCellarSaleSerializer,
            'get_list_pc': ListProductCellarSaleSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return ProductCellarSaleSerializer

    @action(methods=['GET'], detail=False, url_name='list', url_path='list', name='list')
    def get_list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_name='ps', url_path='ps', name='ps')
    def get_list_ps(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_name='pc', url_path='pc', name='pc')
    def get_list_pc(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
