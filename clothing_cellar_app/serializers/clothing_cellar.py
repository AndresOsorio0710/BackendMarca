from rest_framework import serializers
from clothing_cellar_app.models import ClothingCellar
from product_cellar_app.serializers import ProductCellarSerializer
from product_cellar_app.models import ProductCellar


class ClothingCellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingCellar
        fields = '__all__'
        read_only_fields = ['uuid']

    def validate(self, attrs):
        if attrs.get('product_cellar').free_quantity == attrs.get('product_cellar').quantity_entered:
            name = attrs.get('product_cellar').name
            quantity = attrs.get('product_cellar').free_quantity
            raise serializers.ValidationError({
                "status": (
                        "Ya audito el producto " + name + ", " + str(
                    quantity) + " unidades auditadas, y registradas con exito")
            })
        return attrs


class ListClothingProductCellarSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    product_cellar = serializers.CharField()
    name = serializers.CharField()
    cellar = serializers.CharField()
    provider = serializers.CharField()
    reference = serializers.CharField()
    size = serializers.CharField()
    color = serializers.CharField()
    state = serializers.CharField()
    info = serializers.CharField()
