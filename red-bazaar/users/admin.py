from django.contrib import admin
from .models import CustomUser, Profile, Message

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    """ User display for Admin"""

    # Row Display
    list_display = ('id', 'username', 'role', 'email')
    list_display_links = ('id', 'username')

    # Filters
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')


class ProfileAdmin(admin.ModelAdmin):
    """ Profile display for Admin"""

    # Row Display
    list_display = ('id', 'full_name', 'country', 'is_active', 'is_verified')
    list_display_links = ('id', 'full_name')

    # Filters
    list_filter = ('is_active', 'is_verified')
    list_select_related = ('user',)


class MessageAdmin(admin.ModelAdmin):
    """ Profile display for Admin"""

    # Row Display
    list_display = ('id', 'sender', 'recipient', 'subject', 'created_at')
    list_display_links = ('id', 'subject')

    # Filters
    list_filter = ('sender', 'recipient')
    # READ ONLY fields
    readonly_fields = (
        'id', 'sender', 'recipient',
        'subject', 'message', 'created_at',
        'is_read', 'is_deleted_by_sender',
        'is_deleted_by_recipient'
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)
