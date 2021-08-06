from rest_framework import serializers as sz
from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    author = sz.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "created",
            "updated",
            "comment",
            "author",
            "diary",
        )
