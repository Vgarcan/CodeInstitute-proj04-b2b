from django.contrib import admin
from .models import Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    """ Profile display for Admin"""

    # Row Display
    list_display = ('id', 'subject', 'sender', 'recipient', 'created_at')
    list_display_links = ('id', 'subject')

    # Filters
    list_filter = ('created_at',)
    # READ ONLY fields
    readonly_fields = (
        'id', 'sender', 'recipient',
        'subject', 'message', 'created_at',
        'is_read', 'is_deleted_by_sender',
        'is_deleted_by_recipient'
    )


admin.site.register(Message, MessageAdmin)
