from rest_framework import serializers

from base.models import Parent
from base.models import Child


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('id', 'first_name', 'last_name')