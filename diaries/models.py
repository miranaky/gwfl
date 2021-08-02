from django.db import models
from core.models import TimeStapmedModel
from users.models import User
from goodwords.models import GoodWord


class Diary(TimeStapmedModel):

    """Diaries model definition"""

    diary = models.TextField()
    author = models.ForeignKey(User, related_name="diaries", on_delete=models.CASCADE)
    goodwords = models.ForeignKey(GoodWord, related_name="diaries", on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author}_{self.goodwords.title}"

    class Meta:
        verbose_name_plural = "Diaries"

    def count_comments(self):
        return self.comments.count()

    count_comments.short_description = "Number of Comments"
