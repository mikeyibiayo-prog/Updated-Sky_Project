from django.contrib import admin
from .models import Meeting


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display  = ('title', 'date', 'time_start', 'time_end', 'platform', 'organiser')
    list_filter   = ('platform', 'date')
    search_fields = ('title', 'organiser__username')
    filter_horizontal = ('participants',)
