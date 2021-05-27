from rest_framework import viewsets, mixins
from section_app.models import Section
from section_app.serializers import SectionSerializer, ListSectionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class SectionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = super(SectionViewSet, self).get_queryset()
        if self.action == self.get_short.__name__:
            queryset = queryset.only('uuid', 'name', 'icon', 'description')
        return queryset

    def get_serializer_class(self):
        serializer = {
            'get_short': ListSectionSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return SectionSerializer

    @action(methods=['GET'], detail=False, url_name='short', url_path='short', name='short')
    def get_short(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
