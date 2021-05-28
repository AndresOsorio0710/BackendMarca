from rest_framework import serializers
from product_cellar_sale_app.models import ProductCellarSale


class ProductCellarSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCellarSale
        fields = '__all__'
        read_only_fields = ['uuid']


class SaveProductCellarSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCellarSale
        fields = ['product_sale', 'product_cellar', 'quantity']

    def validate(self, attrs):
        attrs.update({
            'cost': attrs.get('product_cellar').unit_cost * attrs.get('quantity')
        })
        return attrs


class ListProductCellarSaleSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    quantity = serializers.IntegerField()
    cost = serializers.FloatField()
    product_sale = serializers.CharField()
    product_cellar = serializers.CharField()
    product_sale_name = serializers.CharField()
    product_sale_price = serializers.FloatField()
    product_cellar_name = serializers.CharField()
    product_cellar_cost = serializers.FloatField()
    product_cellar_quantity = serializers.IntegerField()
