from rest_framework import serializers as sz
from diaries.models import Diary
from comments.serializers import CommentSerializer


class MyDiaryListSerializer(sz.ModelSerializer):
    """ReadDiarySerializer Definition
    ReadDiarySerializer is  Serializer for Personal Diary"""

    comments = sz.IntegerField(source="count_comments", read_only=True)
    goodwords = sz.StringRelatedField(read_only=True)

    class Meta:
        model = Diary
        exclude = ("author",)
        read_only_fields = [
            "comments",
        ]


class MyDiarySerializer(sz.ModelSerializer):
    goodwords = sz.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = [
            "id",
            "created",
            "updated",
            "diary",
            "public",
            "goodwords",
            "comments",
        ]
        read_only_fields = [
            "comments",
            "id",
            "created",
            "goodwords",
        ]


class IsPublicListSerializer(sz.ListSerializer):
    """Serializing for public is true."""

    def to_representation(self, data):
        data = data.filter(public=True)
        return super().to_representation(data)


class ReadDiarySerializer(sz.ModelSerializer):
    """ReadDiarySerializer Definition
    ReadDiarySerializer is  Serializer for Public Diary"""

    goodwords = sz.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    number_of_comments = sz.IntegerField(source="count_comments", read_only=True)

    class Meta:
        model = Diary
        list_serializer_class = IsPublicListSerializer  # filtering public diary.
        fields = [
            "id",
            "created",
            "updated",
            "author",
            "diary",
            "public",
            "goodwords",
            "number_of_comments",
            "comments",
        ]
        read_only_fields = [
            "comments",
            "id",
            "author",
            "created",
            "goodwords",
            "number_of_comments",
        ]
