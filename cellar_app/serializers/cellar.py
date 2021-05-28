from rest_framework import serializers
from cellar_app.models import Cellar


class CellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cellar
        fields = '__all__'
        read_only_fields = ['uuid']


class ListCellarSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    short_name = serializers.CharField()
    name = serializers.CharField()
    free_capacity = serializers.IntegerField()


class SaveCellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cellar
        fields = [
            'name',
            'short_name',
            'max_capacity',
            'address',
            'phone_number',
            'email',
            'description',
        ]

    def validate(self, attrs):
        attrs.update({
            'short_name': attrs.get('short_name').upper(),
            'name': attrs.get('name').upper(),
            'free_capacity': attrs.get('max_capacity')
        })
        return attrs
