import io

from django.contrib import admin
from django.http import FileResponse, HttpResponse
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.urls import path

try:
    from weasyprint import HTML
except Exception:
    HTML = None

from .models import (
    Department,
    Engineer,
    Team,
    TeamMember,
    Repository,
    ContactChannel,
    TeamDependency,
    Message,
    AuditLog,
)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'recipient', 'is_draft', 'created_at')
    list_filter = ('is_draft', 'created_at')
    search_fields = ('subject', 'body', 'sender__username', 'recipient__username')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'stats/',
                self.admin_site.admin_view(self.stats_view),
                name='message_stats'
            ),
        ]
        return custom_urls + urls

    def stats_view(self, request):
        total = Message.objects.count()
        sent = Message.objects.filter(is_draft=False).count()
        drafts = Message.objects.filter(is_draft=True).count()

        context = dict(
            self.admin_site.each_context(request),
            total=total,
            sent=sent,
            drafts=drafts,
        )

        return TemplateResponse(
            request,
            'admin/messages_app/message_stats.html',
            context
        )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'manager')
    list_filter = ('department',)
    search_fields = ('name', 'description', 'department__name')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'report/',
                self.admin_site.admin_view(self.report),
                name='team_report'
            ),
        ]
        return custom_urls + urls

    def report(self, request):
        if HTML is None:
            return HttpResponse(
                "WeasyPrint is not installed correctly. Please check Pango/Homebrew setup.",
                status=500
            )

        teams = Team.objects.select_related('department', 'manager').all().order_by(
            'department__name',
            'name'
        )

        departments = Department.objects.all().order_by('name')

        team_members = TeamMember.objects.select_related(
            'team',
            'engineer'
        ).all().order_by('team__name', 'engineer__full_name')

        dependencies = TeamDependency.objects.select_related(
            'team',
            'depends_on_team'
        ).all().order_by('team__name', 'depends_on_team__name')

        repositories = Repository.objects.select_related(
            'team'
        ).all().order_by('team__name', 'name')

        contact_channels = ContactChannel.objects.select_related(
            'team'
        ).all().order_by('team__name', 'type')

        teams_without_managers = Team.objects.filter(
            manager__isnull=True
        ).select_related('department').order_by('name')

        html_string = render_to_string('messages/team_report.html', {
            'teams': teams,
            'departments': departments,
            'team_members': team_members,
            'dependencies': dependencies,
            'repositories': repositories,
            'contact_channels': contact_channels,
            'teams_without_managers': teams_without_managers,

            'total_teams': teams.count(),
            'total_departments': departments.count(),
            'total_team_members': team_members.count(),
            'total_dependencies': dependencies.count(),
            'total_repositories': repositories.count(),
            'total_contact_channels': contact_channels.count(),
            'teams_without_managers_count': teams_without_managers.count(),
        })

        pdf_file = HTML(string=html_string).write_pdf()
        buffer = io.BytesIO(pdf_file)

        return FileResponse(
            buffer,
            as_attachment=True,
            filename='team_report.pdf'
        )


admin.site.register(Department)
admin.site.register(Engineer)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember)
admin.site.register(Repository)
admin.site.register(ContactChannel)
admin.site.register(TeamDependency)
admin.site.register(Message, MessageAdmin)
admin.site.register(AuditLog)