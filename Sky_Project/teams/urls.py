from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.team_directory, name='directory'),
    path('profile/', views.team_profile, name='profile'),
]
