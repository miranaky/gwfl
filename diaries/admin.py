from django.contrib import admin
from diaries import models
from comments.models import Comment


class CommentInline(admin.TabularInline):

    model = Comment


@admin.register(models.Diary)
class DiariesAdmin(admin.ModelAdmin):

    """Diaries Admin Settings."""

    list_display = ("author", "goodwords", "diary", "date", "count_comments")
    list_filter = ("author",)
    inlines = (CommentInline,)

    # def count_comments(self, obj):
    #     return obj.comments.count()

    def date(self, obj):
        return obj.goodwords.date
