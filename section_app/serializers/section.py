from rest_framework import serializers
from section_app.models import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        read_only_field = ['uuid']

    def validate(self, attrs):
        attrs.update({
            'name': attrs.get('name').upper()
        })
        return attrs


class ListSectionSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    icon = serializers.CharField()
    description = serializers.CharField()
