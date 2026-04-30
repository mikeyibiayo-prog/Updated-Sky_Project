from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.timezone import now
from .models import Meeting


@login_required
def schedule_view(request):
    meetings = Meeting.objects.filter(
        participants=request.user
    ).union(
        Meeting.objects.filter(organiser=request.user)
    ).order_by('date', 'time_start')

    all_meetings = Meeting.objects.filter(
        organiser=request.user
    ) | Meeting.objects.filter(participants=request.user)
    all_meetings = all_meetings.distinct().order_by('date', 'time_start')

    return render(request, 'schedule/schedule.html', {
        'meetings': all_meetings,
        'today': now().date(),
    })


@login_required
def create_meeting(request):
    all_users = User.objects.exclude(id=request.user.id).order_by('username')

    if request.method == 'POST':
        title      = request.POST.get('title', '').strip()
        date       = request.POST.get('date')
        time_start = request.POST.get('time_start')
        time_end   = request.POST.get('time_end')
        platform   = request.POST.get('platform', 'Zoom')
        join_link  = request.POST.get('join_link', '').strip()
        notes      = request.POST.get('notes', '').strip()
        participant_ids = request.POST.getlist('participants')

        if not all([title, date, time_start, time_end]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'schedule/create_meeting.html', {'all_users': all_users})

        meeting = Meeting.objects.create(
            title=title,
            date=date,
            time_start=time_start,
            time_end=time_end,
            platform=platform,
            join_link=join_link or None,
            notes=notes,
            organiser=request.user,
        )
        if participant_ids:
            meeting.participants.set(User.objects.filter(id__in=participant_ids))

        messages.success(request, f'Meeting "{title}" created successfully.')
        return redirect('schedule:schedule')

    return render(request, 'schedule/create_meeting.html', {'all_users': all_users})


@login_required
def edit_meeting(request, meeting_id):
    meeting   = get_object_or_404(Meeting, id=meeting_id, organiser=request.user)
    all_users = User.objects.exclude(id=request.user.id).order_by('username')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'delete':
            title = meeting.title
            meeting.delete()
            messages.success(request, f'Meeting "{title}" deleted.')
            return redirect('schedule:schedule')

        title      = request.POST.get('title', '').strip()
        date       = request.POST.get('date')
        time_start = request.POST.get('time_start')
        time_end   = request.POST.get('time_end')
        platform   = request.POST.get('platform', 'Zoom')
        join_link  = request.POST.get('join_link', '').strip()
        notes      = request.POST.get('notes', '').strip()
        participant_ids = request.POST.getlist('participants')

        if not all([title, date, time_start, time_end]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'schedule/edit_meeting.html', {
                'meeting': meeting, 'all_users': all_users
            })

        meeting.title      = title
        meeting.date       = date
        meeting.time_start = time_start
        meeting.time_end   = time_end
        meeting.platform   = platform
        meeting.join_link  = join_link or None
        meeting.notes      = notes
        meeting.save()
        meeting.participants.set(User.objects.filter(id__in=participant_ids))

        messages.success(request, f'Meeting "{title}" updated.')
        return redirect('schedule:schedule')

    return render(request, 'schedule/edit_meeting.html', {
        'meeting': meeting,
        'all_users': all_users,
    })
