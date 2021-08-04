from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("", views.UserView.as_view()),
    path("login/", views.login_view),
    path("me/", views.MeView.as_view()),
    path("<int:pk>/", views.user_view),
]
