# Generated by Django 4.1.5 on 2023-01-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_WintR', '0003_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='tag',
            field=models.CharField(default='Teambuilding', max_length=100),
            preserve_default=False,
        ),
    ]
