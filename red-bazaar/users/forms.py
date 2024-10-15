from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser, Profile

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


class CustomUserForm(forms.ModelForm):
    """
    A form for editing the CustomUser model.

    This form is used to edit basic user information, specifically the username and email fields.
    It is based on Django's ModelForm and is linked to the CustomUser model.

    Attributes:
        Meta: Defines the model and the fields to be included in the form.
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Fields that will appear in the form


class ProfileForm(forms.ModelForm):
    """
    A form for editing the Profile model.

    This form is used to edit additional user profile information, such as personal details and 
    social media links. It is based on Django's ModelForm and is linked to the Profile model.

    Attributes:
        Meta: Defines the model and the fields to be included in the form.
    """

    class Meta:
        model = Profile
        fields = [
            'full_name', 'country', 'city', 'address', 'postal_code', 'phone_number',
            'bio', 'website', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url'
        ]  # Fields that will appear in the form
