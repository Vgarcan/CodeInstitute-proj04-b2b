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
    ROLES = {
        BUYER: "Buyer",
        SUPPLIER: "Supplier",
    }

    role = models.CharField(max_length=3, choices=ROLES.items(), default=BUYER)

    groups = models.ManyToManyField(Group, related_name='user_set_group')
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_set_permissions'
    )

    def __str__(self):
        """
        Returns a string representation of the CustomUser object.

        The string representation includes the username and role of the user.

        Parameters:
        None

        Returns:
        str: A string in the format 'username, role'.
        """
        return f'{self.username}, {self.role}'
