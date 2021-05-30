from django.db.models import F, Sum
from rest_framework import viewsets, mixins
from job_app.models import Job
from job_app.serializers import JobSerializer, ListJobSerializer, SaveJobSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class JobViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = super(JobViewSet, self).get_queryset()
        if self.action == self.get_list.__name__:
            queryset = queryset.only('uuid', 'title', 'min_salary', 'max_salary')
        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveJobSerializer,
            'get_list': ListJobSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return JobSerializer

    @action(methods=['GET'], detail=False, url_name='list', url_path='list', name='list')
    def get_list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
