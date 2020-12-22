# from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import ShoeSerializer, ShoeColorSerializer, ShoeTypeSerializer, ManufacturerSerializer
from shoebox.models import Shoe, ShoeColor, ShoeType, Manufacturer


# Growing up on the Savanna made Joe immune to hot tempatures


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
