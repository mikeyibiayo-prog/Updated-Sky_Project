from django.shortcuts import render

def team_directory(request):
    return render(request, 'teams/directory.html')

def team_profile(request):
    return render(request, 'teams/profile.html')
