from rest_framework import serializers
from product_sale_app.models import ProductSale
import random


class ProductSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSale
        fields = '__all__'
        read_only_fields = ['uuid']


class ListProductSaleSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    section = serializers.CharField()
    section_name = serializers.CharField()
    collection = serializers.CharField()
    collection_name = serializers.CharField()
    reference = serializers.CharField()
    name = serializers.CharField()
    cost = serializers.FloatField()
    price = serializers.FloatField()
    utility = serializers.FloatField()
    discount = serializers.IntegerField()
    discount_unit = serializers.IntegerField()
    description = serializers.CharField()


class SaveProductSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSale
        fields = ['section', 'collection', 'name', 'description', 'cost', 'price', 'discount', 'discount_unit']
        read_only_field = ['uuid']

    def validate(self, attrs):
        if attrs.get('price') < attrs.get('cost'):
            raise serializers.ValidationError({
                "status": "El precio de venta del producto no puede ser mayor al costo de compra."
            })
        name = attrs.get('name').upper()
        random_1 = random.randint(0, 999)
        random_2 = random.randint(0, 999)
        attrs.update({
            'utility': attrs.get('price') - attrs.get('cost'),
            'reference': "-" + name[0:4] + "-" + "{:0>3}".format(str(random_1)) + "-" + "{:0>3}".format(str(random_2)),
            'name': name
        })
        return attrs
