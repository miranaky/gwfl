from django.db import models


class Calendar(models.Model):
    """Calender Model Definition."""

    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.date}"
