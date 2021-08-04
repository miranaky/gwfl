from rest_framework import serializers
from .models import GoodWord
from calendars.serializers import CalendarSerializer


class GoodWordsSerializer(serializers.ModelSerializer):
    date = CalendarSerializer()

    class Meta:
        model = GoodWord
        fields = ("title", "goodwords", "speaker", "date")
