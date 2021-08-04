from django.urls import path
from goodwords import views

app_name = "goodwords"
urlpatterns = [
    path("list/", views.ListGoodWordsView.as_view()),
]
