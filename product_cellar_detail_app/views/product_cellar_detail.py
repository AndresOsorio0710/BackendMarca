from django.db.models import F, Sum, Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from product_in_cellar_detail_app.models import ProductInCellarDetail
from product_in_cellar_detail_app.serializers import ProductInCellarDetailSerializer, \
    SaveProductInCellarDetailSerializer, ListProductInCellarSerializer, \
    ListLiteProductInCellarDetailSerializer, ListProductInCellarDetailSerializer


class ProductInCellarDetailViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductInCellarDetail.objects.all()
    serializer_class = ProductInCellarDetailSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        queryset = super(ProductInCellarDetailViewSet, self).get_queryset()

        if self.action == self.list.__name__:
            queryset = queryset.values(
                'uuid',
                'type',
                'size',
                'state',
                'info'
            ).annotate(
                product=F('product_in_cellar'),
                name=F('product_in_cellar__name'),
                cellar=F('product_in_cellar__cellar__name'),
                provider=F('product_in_cellar__provider__name'),
                reference=F('product_in_cellar__reference')
            )

        if self.action == self.get_pic.__name__:
            queryset = queryset.filter(
                product_in_cellar=self.kwargs.get('uuid')
            ).values(
                'uuid',
                'type',
                'size',
                'state',
                'info'
            ).annotate(
                product=F('product_in_cellar'),
                name=F('product_in_cellar__name'),
                cellar=F('product_in_cellar__cellar__name'),
                provider=F('product_in_cellar__provider__name'),
                reference=F('product_in_cellar__reference')
            )

        if self.action == self.get_pic_size.__name__:
            queryset = queryset.filter(
                product_in_cellar=self.kwargs.get('uuid')
            ).values('size').annotate(
                free=Count('size'),
            )

        if self.action == self.get_pic_all.__name__:
            queryset = queryset.values('product_in_cellar').annotate(
                name=F('product_in_cellar__name'),
                cellar=F('product_in_cellar__cellar__name'),
                provider=F('product_in_cellar__provider__name'),
                reference=F('product_in_cellar__reference'),
                description=F('product_in_cellar__description'),
                cost=F('product_in_cellar__cost'),
                unit_cost=F('product_in_cellar__unit_cost'),
                quantity=F('product_in_cellar__quantity_entered'),
                free=Count('uuid', distinct=True),
                stop=F('product_in_cellar__stop'),
            )

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductInCellarDetailSerializer,
            'list': ListProductInCellarSerializer,
            'get_pic': ListProductInCellarSerializer,
            'get_pic_all': ListProductInCellarDetailSerializer,
            'get_pic_size': ListLiteProductInCellarDetailSerializer,
        }

        if self.action in serializer:
            return serializer[self.action]

        return ProductInCellarDetailSerializer

    @action(methods=['GET'], detail=True, url_name='pic', url_path='pic', name='pic')
    def get_pic(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_name='pic/size', url_path='pic/size', name='pic/size')
    def get_pic_size(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_name='pic/all', url_path='pic/all', name='pic/all')
    def get_pic_all(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
