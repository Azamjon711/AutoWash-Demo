from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StaffSerializer
from staff.models import Staff
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.db.transaction import atomic


class StaffAPIViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["first_name", "last_name", "email", "username", "position"]
    pagination_class = LimitOffsetPagination

