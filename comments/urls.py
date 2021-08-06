from django.urls import path
from comments.views import CommentView

app_name = "comments"

urlpatterns = [
    path("", CommentView.as_view()),
]
