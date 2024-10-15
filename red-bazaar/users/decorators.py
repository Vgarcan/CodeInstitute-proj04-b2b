from django.core.exceptions import PermissionDenied
from functools import wraps
from django.contrib import messages


def role_required(required_role):
    """
    Decorator to restrict access to users with a specific role.

    Args:
        required_role (str): The required role for the view (e.g., 'SUP', 'BUY').

    Raises:
        PermissionDenied: If the user does not have the required role.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == required_role:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(
                    request, 'There was an error updating your profile.')
                raise PermissionDenied

        return _wrapped_view
    return decorator
