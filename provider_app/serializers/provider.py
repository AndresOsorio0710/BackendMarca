from rest_framework import serializers
from provider_app.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
        read_only_fields = ['uuid']


class ListLiteProviderSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
