from django.contrib import admin
from calendars import models as calendars_models


@admin.register(calendars_models.Calendar)
class CalendarAdmin(admin.ModelAdmin):
    """Calender Admin Settings."""

    list_display = ("date", "goodwords")
    ordering = ["-date"]

    def goodwords(self, obj):
        return obj.goodwords.get(date=obj.pk).title
