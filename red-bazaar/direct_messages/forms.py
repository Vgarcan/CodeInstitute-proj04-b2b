from allauth.account.forms import SignupForm
from django import forms
from .models import Message
from users.models import Profile

# Define the custom form for user signup


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
            'bio', 'profile_picture', 'website', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url'
        ]  # Fields that will appear in the form


class MessageForm(forms.ModelForm):
    """
    A form for sending messages to other users.

    This form is used to collect the recipient's username and the message content. It is based 
    on Django's ModelForm and is linked to the Message model.
    """

    class Meta:
        model = Message
        # Fields that will appear in the form
        fields = ['subject', 'message']
        # Labels for the fields
        labels = {
            'subject': 'Subject',
            'message': 'Message Content'
        }  # Labels for the fields
