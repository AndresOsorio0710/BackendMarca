from rest_framework import serializers
from product_cellar_app.models import ProductCellar
from product_cellar_detail_app.models import ProductCellarDetail
from django.db.models import Count


class ProductCellarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCellarDetail
        fields = '__all__'
        read_only_fields = ['uuid']


class ListProductCellarSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    product = serializers.CharField()
    name = serializers.CharField()
    cellar = serializers.CharField()
    provider = serializers.CharField()
    reference = serializers.CharField()
    type = serializers.CharField()
    size = serializers.CharField()
    state = serializers.CharField()
    info = serializers.CharField()


class ListProductCellarDetailSerializer(serializers.Serializer):
    product_in_cellar = serializers.CharField()
    name = serializers.CharField()
    cellar = serializers.CharField()
    provider = serializers.CharField()
    reference = serializers.CharField()
    description = serializers.CharField()
    cost = serializers.FloatField()
    unit_cost = serializers.FloatField()
    quantity = serializers.IntegerField()
    free = serializers.IntegerField()
    stop = serializers.IntegerField()


class ListLiteProductCellarDetailSerializer(serializers.Serializer):
    size = serializers.CharField()
    free = serializers.IntegerField()


class SaveProductCellarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCellarDetail
        fields = [
            'uuid',
            'product_in_cellar',
            'type',
            'size',
            'color',
            'state',
            'info'
        ]
        read_only_fields = ['uuid']

    def validate(self, attrs):
        if attrs.get('product_cellar').free_quantity == attrs.get('product_cellar').quantity_entered:
            raise serializers.ValidationError({
                "status": "El producto ya fue segcionado y relacionado. "
            })
        return attrs
