from django.db import models
from users.models import CustomUser

# Create your models here.


class Message(models.Model):
    """
    A model to store private messages between users.

    Attributes:
        `sender` (ForeignKey): The user who sends the message.
        `recipient` (ForeignKey): The user who receives the message.
        `subject` (CharField): The subject/title of the message (max length: 255).
        `message` (TextField): The body of the message.
        `created_at` (DateTimeField): The timestamp of when the message was created.
        `is_read` (BooleanField): Indicates if the recipient has read the message.
        `is_deleted_by_sender` (BooleanField): Marks if the sender has deleted the message.
        `is_deleted_by_recipient` (BooleanField): Marks if the recipient has deleted the message.

    Methods:
        __str__(): Returns a string representation of the message in the format:
                   `sender -> recipient: subject`.
    """
    sender = models.ForeignKey(
        CustomUser,
        related_name='sent_messages',
        on_delete=models.CASCADE,
    )
    recipient = models.ForeignKey(
        CustomUser,
        related_name='received_messages',
        on_delete=models.CASCADE,
    )
    subject = models.CharField(
        max_length=255,
    )
    message = models.TextField(
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    is_read = models.BooleanField(
        default=False,
    )
    is_deleted_by_sender = models.BooleanField(
        default=False,
    )
    is_deleted_by_recipient = models.BooleanField(
        default=False,
    )

    def __str__(self):
        """
        Returns a string representation of the message.

        Format:
            sender -> recipient: subject

        Returns:
            str: A string representing the sender, recipient, and subject of the message.
        """
        return f'{self.sender} -> {self.recipient}: {self.subject}'
