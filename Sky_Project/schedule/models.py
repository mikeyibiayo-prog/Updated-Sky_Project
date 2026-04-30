from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    PLATFORM_CHOICES = [
        ('Zoom', 'Zoom'),
        ('Microsoft Teams', 'Microsoft Teams'),
        ('Google Meet', 'Google Meet'),
        ('In Person', 'In Person'),
        ('Other', 'Other'),
    ]

    title        = models.CharField(max_length=255)
    date         = models.DateField()
    time_start   = models.TimeField()
    time_end     = models.TimeField()
    platform     = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='Zoom')
    join_link    = models.URLField(blank=True, null=True)
    notes        = models.TextField(blank=True)
    organiser    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organised_meetings')
    participants = models.ManyToManyField(User, related_name='meetings', blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time_start']

    def __str__(self):
        return f"{self.title} ({self.date})"
