# Generated by Django 4.1.5 on 2023-01-29 02:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('_WintR', '0002_rename_event_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
