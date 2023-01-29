import datetime

from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import _WintR.submissions as submissions

def index(request):
    print(submissions.request_all())
    return HttpResponse(render(request, 'index.html'))

def login_(request):
    # If method is post user is trying to log in
    if request.method =='POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            # Set session cookie and redirect to homepage
            login(request, user)
            return redirect('/')
        else:
            # Wrong login credentials
            return HttpResponse(render(request, 'login.html', context={'error':True, 'error_message':'Username or password is incorrect!'}))
    # Otherwise user is probably requesting the page
    else:
        return HttpResponse(render(request, 'login.html'))

def logout_(request):
    # Log out if logged in
    if request.user.is_authenticated:
        logout(request)
    # Then just redirect to homepage
    return redirect('/')

def signup(request):
    # If method is post user is trying to sign up
    if request.method =='POST':
        username = request.POST['name']
        password = request.POST['password']
        # Protext against XSS and other dumb stuff (also disallow some weird characters)
        if any(c in username for c in '<>/\\\'{}%" \n\t'):
            # Using forbidden characters in username
            return HttpResponse(render(request, 'signup.html', context={'error':True, 'error_message':'Forbidden characters in username'}))
        # Username already exists
        if(User.objects.filter(username=username).exists()):
            return HttpResponse(render(request, 'signup.html', context={'error':True, 'error_message':'Username already in use'}))
        # If username or password too short
        if(len(username) < 3 or len(password) < 3):
            return HttpResponse(render(request, 'signup.html', context={'error':True, 'error_message':'Username and password must be at least 3 characters long'}))

        # Create user
        user = User.objects.create_user(username=username, password=password)
        # Automatically log in user or return error page
        if user:
            # Set session cookie and redirect to homepage
            login(request, user)
            print("login successfull!")
            return redirect('/')
        else:
            # Unknown error
            return HttpResponse(render(request, 'signup.html', context={'error':True, 'error_message':'Unknown error'}))
    # Otherwise user is probably requesting the page
    else:
        return HttpResponse(render(request, 'signup.html'))

def post(request):
    # Submitting new post
    if request.method == 'POST':
        title = request.POST['title']
        author = request.user
        tag = request.POST['tag']
        body = request.POST['body']
        location = request.POST['location']
        date = datetime.datetime.now()
        # Create new post
        submissions.post_submission(title=title, author=author, tag=tag, body=body, location=location, date=date)
        return HttpResponse(render(request, 'index.html'))
    # Requesting page
    else:
        return HttpResponse(render(request, 'post.html'))


def user(request):
    user = User.objects.filter(username=request.GET['u'])[0]
    return HttpResponse(render(request, 'user.html', context={'quser': user}))

def tag(request):
    tag = request.GET['t']
    return HttpResponse(render(request, 'tag.html', context={'tag': tag}))


# JavaScript dynamically loading content while scrolling:
def nextpage(request):
    page = int(request.GET['p'])
    return HttpResponse(render(request, 'submissions.html', context={'submissions': submissions.request_page(page, request)}))

# Dynamically loadind content of specific user:
def user_nextpage(request):
    page = int(request.GET['p'])
    user = User.objects.filter(username=request.GET['u'])[0]
    return HttpResponse(render(request, 'submissions.html', context={'submissions': submissions.request_user_page(user, page, request)}))

# Dynamically loading content of specific tag:
def tag_nextpage(request):
    page = int(request.GET['p'])
    tag = request.GET['t']
    return HttpResponse(render(request, 'submissions.html', context={'submissions': submissions.request_tag_page(tag, page, request)}))

# JavaScript attend or stop attending event without page reload
def attend(request):
    # Get event from event id
    submission_id = request.GET['s']
    submission = submissions.request_id(submission_id)
    submissions.attend(request.user, submission)
    # Return amount of people attending
    return HttpResponse(submission.impressions)