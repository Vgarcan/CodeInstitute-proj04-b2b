from .forms import ChatForm
from django.db.models import Max, F, Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm, ChatForm
from .models import Message
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Max

# Create your views here.


@login_required
def send_message(request, username):
    recipient = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Current user as sender
            message.recipient = recipient  # Profile being viewed as recipient
            message.save()
            return redirect('users:user_profile', recipient.pk)
    else:
        form = MessageForm()

    return render(request, 'messages/send_message.html', {
        'form': form,
        'recipient': recipient,
    })


@login_required
def chat_view(request, recipient_id=None):
    """
    View for displaying the chat interface.

    Retrieves a unique list of conversations for the logged-in user, consolidating all messages between two users into a single conversation.
    Handles message sending and updates the chat interface dynamically.

    Args:
        request: The HTTP request object.
        recipient_id (int): The ID of the recipient user for the current chat session.

    Returns:
        HttpResponse: Renders the chat template with the list of unique conversations and messages.
    """
    # Retrieve unique conversations where the current user is involved
    conversations = (
        Message.objects.filter(Q(sender=request.user) |
                               Q(recipient=request.user))
        .values('sender', 'recipient')
        .distinct()  # Ensure each pair of users appears only once
    )

    # Prepare a dictionary to group conversations
    unique_users = {}
    for convo in conversations:
        # Identify the other user in the conversation
        other_user_id = convo['recipient'] if convo['sender'] == request.user.id else convo['sender']

        # Skip duplicates by ensuring each user pair appears only once
        if other_user_id in unique_users:
            continue

        # Fetch the user object for the other participant
        other_user = CustomUser.objects.get(id=other_user_id)

        # Retrieve the most recent message between the current user and the other user
        last_message = (
            Message.objects.filter(
                Q(sender=request.user, recipient=other_user)
                | Q(sender=other_user, recipient=request.user)
            )
            .order_by('-created_at')
            .first()
        )

        # Add the conversation to the dictionary
        unique_users[other_user_id] = {
            'user': other_user,
            'last_message': last_message.message if last_message else "No messages yet",
        }

    # Get the selected recipient, if any
    recipient = None
    if recipient_id:
        recipient = get_object_or_404(CustomUser, id=recipient_id)

    # Retrieve all messages between the current user and the selected recipient
    messages = []
    if recipient:
        messages = Message.objects.filter(
            Q(sender=request.user, recipient=recipient)
            | Q(sender=recipient, recipient=request.user)
        ).order_by('created_at')

    # Handle form submission for sending a message
    if request.method == 'POST' and recipient:
        form = ChatForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.recipient = recipient
            new_message.save()
            return redirect('direct_messages:chat', recipient_id=recipient.id)
    else:
        form = ChatForm()

    return render(request, 'direct_messages/chat.html', {
        'conversations': unique_users.values(),  # Pass only the unique conversations
        'messages': messages,
        'form': form,
        'recipient': recipient,
    })
