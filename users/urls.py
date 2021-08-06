from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("", views.UserView.as_view()),  # user create.
    path("login/", views.login_view),  # user login.
    path("me/", views.MeView.as_view()),  # show/edit logined user profile.
    path("<int:pk>/", views.user_view),  # show other users profile.
]
