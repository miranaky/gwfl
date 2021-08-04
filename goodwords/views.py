from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import GoodWord
from calendars import models as calendar_models
from .serializers import GoodWordsSerializer


class ListGoodWordsView(ListAPIView):

    queryset = GoodWord.objects.all()
    serializer_class = GoodWordsSerializer
