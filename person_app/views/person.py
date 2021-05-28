from rest_framework import viewsets, mixins
from person_app.models import Person
from person_app.serializers import PersonSerializer, SavePersonSerializer, ListPersonSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PersonViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        queryset = super(PersonViewSet, self).get_queryset()
        if self.action == self.get_list.__name__:
            queryset = queryset.values('uuid', 'id_type', 'id', 'last_name', 'name', 'address', 'phone_number', 'email',
                                       'gender')
        if self.action == self.get_list_id.__name__:
            queryset = queryset.filter(id=self.kwargs.get('uuid')).values('uuid', 'id_type', 'id', 'last_name',
                                                                          'name', 'address', 'phone_number', 'email',
                                                                          'gender')
        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SavePersonSerializer,
            'get_list': ListPersonSerializer,
            'get_list_id': ListPersonSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return PersonSerializer

    @action(methods=['GET'], detail=False, url_name='list', url_path='list', name='list')
    def get_list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_name='id', url_path='id', name='id')
    def get_list_id(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
