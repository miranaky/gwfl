from django.db import models


class TimeStapmedModel(models.Model):
    """custom timespamted model definition."""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
