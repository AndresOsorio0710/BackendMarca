from rest_framework import serializers
from job_app.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['uuid']


class ListJobSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    title = serializers.CharField()
    min_salary = serializers.FloatField()
    max_salary = serializers.FloatField()


class SaveJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'min_salary', 'max_salary']

    def validate(self, attrs):
        if attrs.get('min_salary') > attrs.get('max_salary'):
            raise serializers.ValidationError({
                "status": "El limite de salario minimo debe ser menor o igual al limite de salario maximo."
            })
        attrs.update({
            'title': attrs.get('title').upper()
        })
        return attrs
