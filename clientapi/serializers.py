from rest_framework import serializers
from client.models import Address, Comment, Client


class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    address = AddresSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)

    class Meta:
        model = Client
        fields = "__all__"

