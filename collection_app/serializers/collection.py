from rest_framework import serializers
from collection_app.models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        read_only_field = ['uuid']

    def validate(self, attrs):
        attrs.update({
            'name': attrs.get('name').upper()
        })
        return attrs


class ListCollectionSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    icon = serializers.CharField()
    description = serializers.CharField()
