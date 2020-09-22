from django.contrib import admin
from django.utils.text import Truncator

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": ("url", "message"),
            },
        ),
        (
            "Options",
            {
                "fields": ("is_active", "is_global"),
            },
        ),
    )
    list_display = ("message_display", "is_global", "is_active", "url")
    list_filter = ("is_global", "is_active")

    def message_display(self, obj):
        """
        Truncate message to 50 characters.

        """
        return Truncator(obj.message).chars(50, html=True)

    message_display.allow_tags = True
    message_display.short_description = "Message"
