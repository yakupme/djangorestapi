from rest_framework import serializers
from .models import MobilePhone


class PhoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MobilePhone
        fields = ('id', 'made', 'modelname', 'color', 'release_date')

class PhoneUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobilePhone
        fields = ('id', 'url', 'made', 'modelname', 'color', 'release_date')
        extra_kwargs = {'url': {'view_name': 'phone-detail', 'lookup_field': 'id'}}
