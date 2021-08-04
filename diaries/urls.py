from django.urls import path
from diaries.views import MyDiaryViews

app_name = "diaries"

urlpatterns = [
    path("me/", MyDiaryViews.as_view()),
]
