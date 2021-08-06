from comments.models import Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from comments.serializers import CommentSerializer
from users.models import User
from diaries.models import Diary
from diaries.serializers import ReadDiarySerializer


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_author_and_diaries(self, author_pk, diaries_pk):
        try:
            author = User.objects.get(pk=author_pk)
            diary = Diary.objects.get(pk=diaries_pk)
            return author, diary
        except User.DoesNotExist or Diary.DoesNotExist:
            return None, None

    def post(self, request):
        author, diary = self.get_author_and_diaries(request.user.pk, request.data.get("diary"))
        if author is not None and diary is not None:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=author, diary=diary)
                return Response(ReadDiarySerializer(diary).data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            comment = Comment.objects.get(pk=request.data.get("comment"))
            if comment.author.pk == request.user.pk:
                serializer = CommentSerializer(data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):
        try:
            comment = Comment.objects.get(pk=request.data.get("comment"))
            if comment.author.pk == request.user.pk:
                comment.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
