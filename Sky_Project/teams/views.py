from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def team_directory(request):
    return render(request, 'teams/directory.html')

@login_required
def team_profile(request):
    return render(request, 'teams/profile.html')
