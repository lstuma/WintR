import datetime
from _WintR.models import submission

def request_page(page, request):
    # Grab 20 submissions
    posts = submission.objects.all().order_by('-date')[page*20:page*20+20]
    return((post, is_attending(request.user, post)) for post in posts)

def request_user_page(user, page, request):
    # Grab 20 submissions
    posts = submission.objects.filter(author=user).order_by('-date')[page*20:page*20+20]
    return ((post, is_attending(request.user, post)) for post in posts)

def request_tag_page(tag, page, request):
    # Grab 20 submissions
    posts = submission.objects.filter(tag=tag).order_by('-date')[page*20:page*20+20]
    return ((post, is_attending(request.user, post)) for post in posts)

def request_id(id):
    # Return post with specific id
    return submission.objects.filter(submission_id=id)[0]

def request_all():
    # Return all posts
    return submission.objects.all()

def post_submission(title, author, tag, body, location, date):
    # Create evet submission
    event = submission(title=title, author=author, tag=tag, body=body, location=location, date=date, impressions=0)
    # Save the event submission
    event.save()

def attend(user, submission):
    # Add user to attending userlist
    if not is_attending(user, submission):
        submission.impressions += 1
        submission.attendees.add(user)
    # If already attending, remove user from attending userlist
    else:
        submission.impressions -= 1
        submission.attendees.remove(user)
    submission.save()
def is_attending(user, submission):
    return submission.attendees.filter(username=user.username).exists()
