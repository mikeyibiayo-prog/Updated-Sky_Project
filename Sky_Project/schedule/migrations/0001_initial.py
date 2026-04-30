from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id',         models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title',      models.CharField(max_length=255)),
                ('date',       models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end',   models.TimeField()),
                ('platform',   models.CharField(
                    choices=[('Zoom','Zoom'),('Microsoft Teams','Microsoft Teams'),
                             ('Google Meet','Google Meet'),('In Person','In Person'),('Other','Other')],
                    default='Zoom', max_length=50)),
                ('join_link',  models.URLField(blank=True, null=True)),
                ('notes',      models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('organiser',  models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='organised_meetings',
                                                  to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, related_name='meetings',
                                                         to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['date', 'time_start']},
        ),
    ]
