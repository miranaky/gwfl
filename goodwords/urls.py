from django.urls import path
from goodwords import views

app_name = "goodwords"


urlpatterns = [
    path("", views.goodwords_view),
    path("<yyyymmdd:date>/", views.goodword_view),
]
