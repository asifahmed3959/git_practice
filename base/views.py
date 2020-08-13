from django.shortcuts import Http404

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from base.models import Parent
from base.models import Child

from .serializers import UserListSerializer
from .serializers import ChildSerializer


class UserModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Parent.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'parent_id'

    def get_object(self):
        obj = self.queryset.filter(id=self.kwargs.get('parent_id')).first()

        if obj is None:
            raise Http404

        return obj