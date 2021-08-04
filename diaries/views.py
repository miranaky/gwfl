from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from diaries.serializers import MyDiarySerializer
from diaries.models import Diary


class MyDiaryViews(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        diaries = Diary.objects.all()
        serializer = MyDiarySerializer(diaries, many=True).data
        return Response(serializer)
