from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AddressSerializer, CitySerializer, CountrySerializer, LocationSerializer
from location.models import Address, City, Country, Location
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.db.transaction import atomic


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class LocationAPIViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name", "address", "city", "country"]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["POST"])
    def add(self, request, *args, **kwargs):
        location = self.get_object()
        with atomic():
            location.branch += 1
            location.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


