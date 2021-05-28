from rest_framework import serializers
from person_app.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ['uuid']


class SavePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id_type', 'id', 'last_name', 'name', 'address', 'phone_number', 'email', 'gender']
        read_only_fields = ['uuid']

    def validate(self, attrs):
        attrs.update({
            'name': attrs.get('name').upper(),
            'last_name': attrs.get('last_name').upper(),
            'address': attrs.get('address').upper()
        })
        return attrs


class ListPersonSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    id_type = serializers.CharField()
    id = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    gender = serializers.CharField()
