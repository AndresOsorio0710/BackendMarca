from django.db.models import F
from rest_framework import viewsets, mixins
from product_sale_app.models import ProductSale
from product_sale_app.serializers import SaveProductSaleSerializer, ListProductSaleSerializer, ProductSaleSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class ProductSaleViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductSale.objects.all()
    serializer_class = ProductSaleSerializer

    def get_queryset(self):
        queryset = super(ProductSaleViewSet, self).get_queryset()
        if self.action == self.get_list.__name__:
            queryset = queryset.values(
                'uuid',
                'reference',
                'name',
                'cost',
                'price',
                'utility',
                'discount',
                'discount_unit',
                'description'
            ).annotate(
                section_name=F('section__name'),
                section=F('section'),
                collection_name=F('collection__name'),
                collection=F('collection')
            )
        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductSaleSerializer,
            'get_list': ListProductSaleSerializer
        }

        if self.action in serializer:
            return serializer[self.action]
        return ProductSaleSerializer

    @action(methods=['GET'], detail=False, url_name='plist', url_path='list', name='list')
    def get_list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
