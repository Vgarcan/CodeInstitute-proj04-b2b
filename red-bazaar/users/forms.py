from allauth.account.forms import SignupForm
from django import forms

# Define the custom form for user signup


class CustomSignupForm(SignupForm):
    """
    Extends SignupForm from ALLAUTH.
    Adds additional fields to the signup form for user registration.

    > REQUIRED:  'from allauth.account.forms import SignupForm'

    Attributes:
        role (str): The user's role, either 'BUY' or 'SUP'.
    """

    role = forms.ChoiceField(
        choices=[
            ('BUY', 'Buyer'),
            ('SUP', 'Supplier')
        ],
        label='Role')

    def signup(self, request, user):
        """
        Save the additional fields to the user model.

        Args:
            request: The HTTP request object.
            user: The user instance being created.

        Returns:
            user: The updated user instance.
        """
        user.role = self.cleaned_data['role']
        user.save()
        return user
