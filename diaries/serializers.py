from rest_framework import serializers as sz
from diaries.models import Diary


class MyDiarySerializer(sz.ModelSerializer):
    """ReadDiarySerializer Definition
    ReadDiarySerializer is  Serializer for Personal Diary"""

    comments = sz.IntegerField(source="count_comments", read_only=True)

    class Meta:
        model = Diary
        exclude = (
            "id",
            "author",
        )
        read_only_fields = [
            "comments",
        ]


class IsPublicListSerializer(sz.ListSerializer):
    """Serializing for public is true."""

    def to_representation(self, data):
        data = data.filter(public=True)
        return super().to_representation(data)


class ReadDiarySerializer(sz.ModelSerializer):
    """ReadDiarySerializer Definition
    ReadDiarySerializer is  Serializer for Public Diary"""

    comments = sz.IntegerField(source="count_comments", read_only=True)

    class Meta:
        model = Diary
        exclude = ("id",)
        list_serializer_class = IsPublicListSerializer  # filtering public diary.
