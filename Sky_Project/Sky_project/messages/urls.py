from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent, name='sent'),
    path('draft/', views.draft, name='draft'),
    path('new/', views.new_message, name='new_message'),

    path('search/', views.search_messages, name='search_messages'),

    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),

    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('message/<int:message_id>/send-draft/', views.send_draft, name='send_draft'),
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('message/<int:message_id>/edit-draft/', views.edit_draft, name='edit_draft'),
]