from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('',                        views.schedule_view,  name='schedule'),
    path('create/',                 views.create_meeting, name='create_meeting'),
    path('<int:meeting_id>/edit/',  views.edit_meeting,   name='edit_meeting'),
]
