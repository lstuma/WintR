# Generated by Django 4.1.5 on 2023-01-29 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_WintR', '0006_rename_attendees_submission_impressions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='eventId',
            new_name='submissionId',
        ),
    ]
