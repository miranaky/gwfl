from django.contrib import admin
from goodwords import models


@admin.register(models.BackgroundPhoto)
class BackgroundPhotoAdmin(admin.ModelAdmin):

    """Background Photo Admin settings."""

    pass


class PhotoInline(admin.TabularInline):
    model = models.BackgroundPhoto


@admin.register(models.GoodWord)
class GoodWordsAdmin(admin.ModelAdmin):

    """Good Words Admin Settgins."""

    inlines = (PhotoInline,)
    list_display = ("date", "title", "speaker", "goodwords", "count_diaries")
