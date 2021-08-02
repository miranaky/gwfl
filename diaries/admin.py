from django.contrib import admin
from diaries import models


@admin.register(models.Diary)
class DiariesAdmin(admin.ModelAdmin):

    """Diaries Admin Settings."""

    list_display = ("author", "goodwords", "created", "updated", "date", "count_comments")
    list_filter = ("author",)

    # def count_comments(self, obj):
    #     return obj.comments.count()

    def date(self, obj):
        return obj.goodwords.date
