from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from diaries.serializers import MyDiaryListSerializer, MyDiarySerializer, ReadDiarySerializer
from diaries.models import Diary
from users.models import User
from goodwords.models import GoodWord
from calendars.models import Calendar


class MyDiaryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        diaries = Diary.objects.filter(author=request.user.pk)
        serializer = MyDiaryListSerializer(diaries, many=True).data
        return Response(serializer)

    def post(self, request):
        try:
            user = User.objects.get(pk=request.user.pk)
            goodword = GoodWord.objects.get(pk=request.data.get("goodwords"))
        except User.DoesNotExist or GoodWord.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = MyDiarySerializer(data=request.data)
        if serializer.is_valid():
            diary = serializer.save(author=user, goodwords=goodword)
            return Response(MyDiarySerializer(diary).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyDiaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get_diary(self, diary_pk, user_pk):
        try:
            diary = Diary.objects.get(author=user_pk, pk=diary_pk)
            return diary
        except Diary.DoesNotExist:
            return None

    def get(self, request, pk):
        diary = self.get_diary(pk, request.user.pk)
        if diary is not None:
            serializer = MyDiarySerializer(diary).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        diary = self.get_diary(pk, request.user.pk)
        if diary is not None:
            serializer = MyDiarySerializer(diary, data=request.data, partial=True)
            if serializer.is_valid():
                diary = serializer.save()
                return Response(MyDiarySerializer(diary).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        diary = self.get_diary(pk, request.user.pk)
        if diary is not None:
            diary.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def daily_diary_view(request, date):
    try:
        _date = Calendar.objects.get(date=date)
        goodword = GoodWord.objects.get(date=_date)
        diaries = Diary.objects.filter(goodwords=goodword)
        serializer = ReadDiarySerializer(diaries, many=True).data
        return Response(serializer)
    except Calendar.DoesNotExist or GoodWord.DoesNotExist or Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def public_diary_view(request, pk):
    try:
        diary = Diary.objects.get(pk=pk)
        serializer = ReadDiarySerializer(diary).data
        return Response(serializer)
    except Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
