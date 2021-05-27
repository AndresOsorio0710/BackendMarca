from rest_framework import serializers
from clothing_cellar_app.models import ClothingCellar


class ClothingCellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingCellar
        fields = '__all__'
        read_only_fields = ['uuid']


class SaveClothingCellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingCellar
        fields = ['uuid', 'product_cellar', 'size', 'color', 'state', 'info']
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


class ListClothingCellarSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    product_cellar = serializers.CharField()
    size = serializers.CharField()
    color = serializers.CharField()
    state = serializers.CharField()
    info = serializers.CharField()


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


class ListClothingCellarGroupSizeSerializer(serializers.Serializer):
    size = serializers.CharField()
    free = serializers.IntegerField()


class ListClothingCellarGroupColorSerializer(serializers.Serializer):
    size = serializers.CharField()
    color = serializers.CharField()
    free = serializers.IntegerField()
