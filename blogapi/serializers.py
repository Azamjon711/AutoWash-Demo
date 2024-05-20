from rest_framework import serializers
from blog.models import Date, Year, Creator, Comments, BlogPost


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = "__all__"


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class BlogPostSerializer(serializers.ModelSerializer):
    date = DateSerializer(read_only=True)
    year = YearSerializer(read_only=True)
    creator = CreatorSerializer(read_only=True)
    comment = CommentsSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = "__all__"


