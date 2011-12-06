from django.contrib import admin

from soapbox.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_global', 'is_active', 'url')
    list_filter = ('is_global', 'is_active')


admin.site.register(Message, MessageAdmin)
