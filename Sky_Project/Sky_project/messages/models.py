# Imports Django's model tools so database tables can be created.
from django.db import models

# Imports Django's built-in User model for login users.
from django.contrib.auth.models import User


# Stores departments in the organisation.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    # Links a department to a user who manages it.
    department_admin_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_departments'
    )

    # Automatically records when the department was created.
    department_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Stores engineer details.
class Engineer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    job_title = models.CharField(max_length=100, blank=True)
    slack_user_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name


# Stores teams and links them to departments.
class Team(models.Model):
    name = models.CharField(max_length=100)

    # Each team belongs to one department.
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teams'
    )

    description = models.TextField(blank=True)

    # Optional manager linked through TeamMember.
    manager = models.ForeignKey(
        'TeamMember',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_teams'
    )

    def __str__(self):
        return self.name


# Links engineers to teams and stores their role.
class TeamMember(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='members'
    )

    engineer = models.ForeignKey(
        Engineer,
        on_delete=models.CASCADE,
        related_name='team_memberships'
    )

    role_in_team = models.CharField(max_length=100, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.engineer.full_name} - {self.team.name}"


# Stores code repositories linked to teams.
class Repository(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='repositories'
    )

    name = models.CharField(max_length=100)
    repository_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# Stores contact methods for teams, such as email or Slack.
class ContactChannel(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='contact_channels'
    )

    type = models.CharField(max_length=50)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team.name} - {self.type}"


# Stores dependencies between teams.
class TeamDependency(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='dependencies'
    )

    # Links to the team being depended on.
    depends_on_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='depended_on_by'
    )

    dependency_type = models.CharField(max_length=100)
    team_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.team.name} depends on {self.depends_on_team.name}"


# Stores messages between users.
class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )

    subject = models.CharField(max_length=200)
    body = models.TextField()

    # Separates draft messages from sent messages.
    is_draft = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


# Stores actions made in the system for audit tracking.
class AuditLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='audit_logs'
    )

    entity_type = models.CharField(max_length=100)
    entity_id = models.IntegerField()
    changed_at = models.DateTimeField()
    audit_actions = models.CharField(max_length=50)
    audit_changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entity_type} - {self.audit_actions}"