from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from . import serializers
from .models import MobilePhone
# Create your views here.

@api_view(['GET'])

def api_root(request, format=None):
    return Response({
        'Phones': reverse('phones', request=request),

    })


class PhoneView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MobilePhone.objects.all()
    serializer_class = serializers.PhoneSerializer
    lookup_field = 'id'


class PhonesListViewSet(generics.ListCreateAPIView):
    queryset = MobilePhone.objects.all()
    serializer_class = serializers.PhoneUpdateSerializer