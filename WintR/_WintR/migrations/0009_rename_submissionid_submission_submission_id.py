# Generated by Django 4.1.5 on 2023-01-29 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_WintR', '0008_submission_attendees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='submissionId',
            new_name='submission_id',
        ),
    ]
