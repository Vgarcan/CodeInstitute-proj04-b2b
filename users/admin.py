from django.contrib import admin
from .models import CustomUser, Profile

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    """User display for Admin"""

    # Row Display
    list_display = (
        "id",
        "username",
        "role",
        "email"
    )
    list_display_links = ("id", "username")

    # Filters
    list_filter = ("role", "is_staff", "is_superuser")
    search_fields = ("username", "email")


class ProfileAdmin(admin.ModelAdmin):
    """Profile display for Admin"""

    # Row Display
    list_display = (
        "id",
        "full_name",
        "country",
        "is_active",
        "is_verified"
    )
    list_display_links = ("id", "full_name")

    # Filters
    list_filter = ("is_active", "is_verified")
    list_select_related = ("user",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
