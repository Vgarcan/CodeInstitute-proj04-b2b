from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    """
    Extends Django's AbstractUser to add a 'role' field for differentiating user types.

    Fields:
    - `role`: Defines whether the user is a 'Buyer' or 'Supplier'.
    - `groups` and `user_permissions`: Override default fields to avoid conflicts with related names.

    Constants:
    - `BUYER`: Represents a buyer user.
    - `SUPPLIER`: Represents a supplier user.

    Note: The 'profile' field can be added later if needed to link with a Profile model.

    Methods:
    - `__str__`: Returns the username and role for display.
    """

    BUYER = "BUY"
    SUPPLIER = "SUP"
    STAFF = "STAFF"
    ROLES = {
        BUYER: "Buyer",
        SUPPLIER: "Supplier",
    }

    role = models.CharField(max_length=5, choices=ROLES.items())

    groups = models.ManyToManyField(Group, related_name='user_set_group')
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_set_permissions'
    )

    def save(self, *args, **kwargs):
        """
        Overriding the save method to automatically set the username to lowercase.
        """
        self.username = self.username.lower()
        print(self.is_superuser, '----', self.is_staff)
        #! NOT WORKING
        if self.is_superuser or self.is_staff:
            self.role = self.STAFF
        #!############
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the CustomUser object.

        The string representation includes the username and role of the user.

        Parameters:
        None

        Returns:
        str: A string in the format 'username, role'.
        """
        return f'{self.username}'


class Profile(models.Model):
    """
    A model to store additional information about a user, such as personal details, social media links, and profile settings.

    Fields:
    - `user`: A one-to-one relationship with the `CustomUser` model, linking each profile to a specific user.
    - `full_name`: The user's full name (optional).
    - `country`: The user's country of residence (optional).
    - `city`: The user's city of residence (optional).
    - `address`: The user's address (optional).
    - `postal_code`: The user's postal code (optional).
    - `phone_number`: The user's phone number (optional, but not recommended to store as an integer).
    - `profile_picture`: An image field for storing the user's profile picture (optional).
    - `bio`: A short biography or description of the user (optional).
    - `website`: The user's personal or business website URL (optional).
    - `facebook_url`, `twitter_url`, `instagram_url`, `linkedin_url`: URLs to the user's social media profiles (optional).
    - `created_at`: Timestamp of when the profile was created (auto-generated).
    - `updated_at`: Timestamp of when the profile was last updated (auto-generated).
    - `is_active`: A flag indicating whether the profile is active (default is `True`).
    - `is_verified`: A flag indicating whether the user's profile is verified (default is `False`).

    Methods:
    - `__str__`: Returns a string representation of the Profile object, showing the username and role associated with the user.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.IntegerField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the Profile object.
        """
        return f'{self.user.username} - {self.user.role}'
