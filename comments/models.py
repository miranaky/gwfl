from django.db import models
from core.models import TimeStapmedModel
from users.models import User
from diaries.models import Diary


class Comment(TimeStapmedModel):
    """Comment Model Definition."""

    comment = models.TextField()
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    diary = models.ForeignKey(Diary, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} says : {self.comment}"
