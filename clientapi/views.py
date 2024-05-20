from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AddresSerializer, CommentSerializer, ClientSerializer
from client.models import Address, Client, Comment
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
    serializer_class = AddresSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["text"]
    pagination_class = LimitOffsetPagination


class ClientAPIViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["first_name", "last_name", "username", "email", "profession"]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["GET"])
    def count(self, request, *args, **kwargs):
        comment = self.get_object()
        with atomic():
            comment.comment_count += 1
            comment.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["GET"])
    def top(self, request, *args, **kwargs):
        comments = self.get_queryset()
        comments = comments.order_by("-comment_count")[:2]
        serializer = ClientSerializer(comments, many=True)
        return Response(data=serializer.data)

