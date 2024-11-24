from .models import Message, CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ChatForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm, ChatForm
from .models import Message
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
    Handles message sending, marks messages as read when the conversation is accessed, and updates the chat interface dynamically.

    Args:
        request: The HTTP request object.
        recipient_id (int): The ID of the recipient user for the current chat session.

    Returns:
        HttpResponse: Renders the chat template with the list of unique conversations and messages.
    """
    # Retrieve unique conversations involving the current user
    conversations = (
        Message.objects.filter(
            Q(sender=request.user) |
            Q(recipient=request.user)
        )
        .values('sender', 'recipient')
        .distinct()
    )

    # Prepare a dictionary to group conversations by unique users
    unique_users = {}
    for convo in conversations:
        # Determine the other user in the conversation
        other_user_id = convo['recipient'] if convo['sender'] == request.user.id else convo['sender']

        # Skip duplicates by ensuring each user appears only once
        if other_user_id in unique_users:
            continue

        # Fetch the user object for the other participant
        other_user = CustomUser.objects.get(id=other_user_id)

        # Retrieve the most recent message in the conversation
        last_message = (
            Message.objects.filter(
                Q(sender=request.user, recipient=other_user)
                | Q(sender=other_user, recipient=request.user)
            )
            .order_by('-created_at')
            .first()
        )

        # Add the conversation details to the dictionary
        unique_users[other_user_id] = {
            'user': other_user,
            'last_message': last_message.message if last_message else "No messages yet",
            'last_message_time': last_message.created_at if last_message else None,
        }

    # If a recipient ID is provided, fetch the recipient
    recipient = None
    if recipient_id:
        recipient = get_object_or_404(CustomUser, id=recipient_id)

    # Fetch messages between the logged-in user and the selected recipient
    messages = []
    if recipient:
        messages = Message.objects.filter(
            Q(sender=request.user, recipient=recipient)
            | Q(sender=recipient, recipient=request.user)
        ).order_by('created_at')

        # Mark all unread messages as read
        unread_messages = messages.filter(
            recipient=request.user, is_read=False)
        unread_messages.update(is_read=True)

    # Handle message sending
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

    # Render the chat template with the context data
    return render(request, 'direct_messages/chat.html', {
        # Sort conversations by the latest message time
        'conversations': sorted(unique_users.values(), key=lambda x: x['last_message_time'], reverse=True),
        'messages': messages,
        'form': form,
        'recipient': recipient,
    })
