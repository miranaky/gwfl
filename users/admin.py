from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "gender",
        "in_voucher",
        "end_of_voucher",
    )
    list_filter = ("voucher",)
    ordering = ["pk"]

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "avatar",
                    "gender",
                    "birth",
                )
            },
        ),
        (
            "Pay Info",
            {
                "fields": (
                    "voucher",
                    "end_of_voucher",
                )
            },
        ),
        (
            "Logs",
            {"fields": ("date_joined", "last_login")},
        ),
    )
