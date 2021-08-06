from django.db import models


class BackgroundPhoto(models.Model):
    """BackgroundPhoto Model Definition"""

    caption = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="goodword/backgrounds", blank=True)
    goodword = models.ForeignKey("GoodWord", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class GoodWord(models.Model):
    """Good words Model Definition"""

    title = models.CharField(max_length=120)
    goodwords = models.TextField()
    speaker = models.CharField(max_length=120)
    date = models.ForeignKey("calendars.Calendar", related_name="goodwords", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Good Words"

    def __str__(self):
        return f"{self.date} {self.title}"

    def count_diaries(self):
        return self.diaries.count()

    count_diaries.short_description = "Number of Diaries"
