from django.urls import path
from diaries.views import MyDiaryListView, MyDiaryView, daily_diary_view, public_diary_view

app_name = "diaries"

urlpatterns = [
    path("me/", MyDiaryListView.as_view()),
    path("me/<int:pk>/", MyDiaryView.as_view()),
    path("<yyyymmdd:date>/", daily_diary_view),
    path("<int:pk>/", public_diary_view),
]
