from allauth.account.forms import SignupForm
from django import forms
from .models import Message
from users.models import Profile

# Define the custom form for user signup


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


class ChatForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        widgets = {
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type your message here...',
            }),
        }
