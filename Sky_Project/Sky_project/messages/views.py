from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message
from django.http import JsonResponse


@login_required
def inbox(request):
    inbox_messages = Message.objects.filter(
        recipient=request.user,
        is_draft=False
    ).order_by('-created_at')

    return render(request, 'messages/inbox.html', {
        'inbox_messages': inbox_messages
    })


@login_required
def sent(request):
    sent_messages = Message.objects.filter(
        sender=request.user,
        is_draft=False
    ).order_by('-created_at')

    return render(request, 'messages/sent.html', {
        'sent_messages': sent_messages
    })


@login_required
def draft(request):
    draft_messages = Message.objects.filter(
        sender=request.user,
        is_draft=True
    ).order_by('-created_at')

    return render(request, 'messages/draft.html', {
        'draft_messages': draft_messages
    })


@login_required
def new_message(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        is_draft = request.POST.get('is_draft') == 'on'

        try:
            recipient = User.objects.get(username=recipient_username)

            Message.objects.create(
                sender=request.user,
                recipient=recipient,
                subject=subject,
                body=body,
                is_draft=is_draft
            )

            if is_draft:
                messages.success(request, 'Message saved as draft.')
                return redirect('messages:draft')

            messages.success(request, 'Message sent successfully.')
            return redirect('messages:sent')

        except User.DoesNotExist:
            messages.error(request, 'Recipient username was not found.')

    return render(request, 'messages/new_messages.html')


@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    return render(request, 'messages/message_detail.html', {
        'message': message
    })


@login_required
def send_draft(request, message_id):
    draft_message = get_object_or_404(
        Message,
        id=message_id,
        sender=request.user,
        is_draft=True
    )

    draft_message.is_draft = False
    draft_message.save()

    messages.success(request, 'Draft message sent successfully.')
    return redirect('messages:sent')


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    if message.sender == request.user or message.recipient == request.user:
        message.delete()
        messages.success(request, 'Message deleted.')
        return redirect('messages:inbox')

    messages.error(request, 'You cannot delete this message.')
    return redirect('messages:inbox')


@login_required
def edit_draft(request, message_id):
    draft_message = get_object_or_404(
        Message,
        id=message_id,
        sender=request.user,
        is_draft=True
    )

    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        try:
            recipient = User.objects.get(username=recipient_username)

            draft_message.recipient = recipient
            draft_message.subject = subject
            draft_message.body = body
            draft_message.save()

            messages.success(request, 'Draft updated.')
            return redirect('messages:draft')

        except User.DoesNotExist:
            messages.error(request, 'Recipient username was not found.')

    return render(request, 'messages/edit_draft.html', {
        'message': draft_message
    })


@login_required
def search_messages(request):
    query = request.GET.get('query', '')

    results = Message.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user),
        Q(subject__icontains=query) |
        Q(body__icontains=query) |
        Q(sender__username__icontains=query) |
        Q(recipient__username__icontains=query)
    ).order_by('-created_at')

    return render(request, 'messages/search_results.html', {
        'query': query,
        'results': results
    })

@login_required
def search_suggestions(request):
    query = request.GET.get('query', '')

    messages_found = Message.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user),
        Q(subject__icontains=query) | Q(body__icontains=query)
    )[:5]

    suggestions = [message.subject for message in messages_found]

    return JsonResponse({
        'suggestions': suggestions
    })