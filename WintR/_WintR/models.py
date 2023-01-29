from django.db import models
from django.contrib.auth.models import User

class submission(models.Model):
    # Id
    submission_id = models.AutoField(primary_key=True)
    # Title of submission
    title = models.CharField(max_length=100)
    # Author
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Tag ("coding", "teambuilding", "hackathon", ...) only one though
    tag = models.CharField(max_length=100)
    # Body of submission (long and detailed descriptive text)
    body = models.CharField(max_length=5000)
    # Location (either "Online" or an actual location)
    location = models.CharField(max_length=200)
    # Publification date
    date = models.DateTimeField()
    # Amount of people attending the event/ ...?
    impressions = models.IntegerField()
    # List of users attending the event
    attendees = models.ManyToManyField(User, 'attendee')