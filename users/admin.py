from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """Custom User Admin"""

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "gender",
        "voucher",
        "end_of_voucher",
    )
    list_filter = ("voucher",)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "username",
                    "email",
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
