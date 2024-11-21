from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

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
