from rest_framework.viewsets import ModelViewSet
from .serializers import DateSerializer, YearSerializer, CreatorSerializer, CommentsSerializer, BlogPostSerializer
from blog.models import Date, Year, Creator, Comments, BlogPost
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.db.transaction import atomic


class DateAPIViewSet(ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["date"]
    pagination_class = LimitOffsetPagination


class YearAPIViewSet(ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["year"]
    pagination_class = LimitOffsetPagination


class CreatorAPIViewSet(ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name", "description"]
    pagination_class = LimitOffsetPagination


class CommentsAPIViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["client__first_name", "text"]
    pagination_class = LimitOffsetPagination


class BlogPostAPIViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title", "text", "category"]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["GET"])
    def view(self, request, *args, **kwargs):
        posts = self.get_object()
        with atomic():
            posts.views += 1
            posts.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["GET"])
    def top(self, request, *args, **kwargs):
        posts = self.get_queryset()
        posts = posts.order_by("-views")[:2]
        serializer = BlogPostSerializer(posts, many=True)
        return Response(data=serializer.data)


