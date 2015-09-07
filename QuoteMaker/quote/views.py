from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, Http404
from .form_utilities import *
from .models import *
import datetime
import json
import time


def login_view(request):
    """
    Presents a simple form for logging in a user.
    If requested via POST, looks for the username and password,
    and attempts to log the user in. If the credentials are invalid,
    it passes an error message to the context which the template will
    render using a Bootstrap alert.

    :param request: The Django request object.
    :return: The rendered 'login' page.
    """
    context = {'navbar':'login'}
    if request.POST:
        user, message = login_user_from_form(request, request.POST)
        if user:
            return redirect('quote:home')
        elif message:
            context['error_message'] = message
    return render(request, 'login.html', context)


def login_user_from_form(request, body):
    """
    Validates a user's login credentials and returns a tuple
    containing either a valid, logged-in user or a failure
    message.

    Checks if all fields were supplied, then attempts to authenticate,
    then checks if the 'remember' checkbox was checked. If it was, sets
    the cookie's expiration to 0, meaning it will be invalidated when the
    session ends.

    :param request: The Django request object.
    :return: The rendered 'login' page.
    """
    email = body.get("email")
    password = body.get("password")
    if not all([email, password]):
        return None, "You must provide an email and password."
    email = email.lower()  # all emails are lowercase in the database.
    user = authenticate(username=email, password=password)
    remember = body.get("remember")
    if user is None:
        return None, "Invalid username or password."
    login(request, user)
    if remember is not None:
        request.session.set_expiry(0)
    return user, None


def logout_view(request):
    """
    Logs the user out and redirects the user to the login page.
    :param request: The Django request.
    :return: A 301 redirect to the login page.
    """
    logout(request)
    return redirect('quote:login')


def signup(request):
    """
    Presents a simple signup page with a form of all the required
    fields for new users.
    Uses the full_signup_context function to populate a year/month/day picker
    and, if the user was created successfully, prompts the user to log in.
    :param request:
    :return:
    """
    context = {}
    context['is_signup'] = True
    if request.POST:
        user, message = handle_user_form(request, request.POST)
        if user:
            return redirect('quote:login')
        elif message:
            context['error_message'] = message
    context['navbar'] = 'signup'
    return render(request, 'signup.html', context)

def handle_user_form(request, body, user=None):
    """
    Creates a user and validates all of the fields, in turn.
    If there is a failure in any validation, the returned tuple contains
    None and a failure message.
    If validation succeeds and the user can be created, then the returned tuple
    contains the user and None for a failure message.
    :param body: The POST body from the request.
    :return: A tuple containing the User if successfully created,
             or a failure message if the operation failed.
    """
    password = body.get("password")
    first_name = body.get("first_name")
    last_name = body.get("last_name")

    email = body.get("email").lower()  # lowercase the email before adding it to the db.
    if not email_is_valid(email):
        return None, "Invalid email."
    if user:
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return user, None
    else:
        if User.objects.filter(email=email).exists():
            return None, "A user with that email already exists."
        user = User.objects.create_user(email, email=email,
            password=password, first_name=first_name, last_name=last_name)
        if user is None:
            return None, "We could not create that user. Please try again."
        request.user = user
        return user, None


def quote(request, path):
    character = get_object_or_404(Homestarkov, path=path)
    return render(request, 'quote.html', {'user': request.user, 'character': character})


@login_required
def create(request):
    context = {'user': request.user}
    if request.POST:
        character, error = handle_create_quotemaker(request, request.POST)
        if character:
            return redirect('quote:quote', path=character.path)
        elif error:
            context['error_message'] = error
        else:
            context['error_message'] = 'Could not create quotemaker. Try again.'
    raise Http404

def handle_create_quotemaker(request, body):
    name = body.get('name', '').strip()
    tagline = body.get('tagline', '').strip()
    corpus = body.get('corpus', '').strip()
    if not all([name, body, corpus]):
        return None, "All fields are required"
    path = name.lower().replace(" ", '-')
    character = Homestarkov.objects.create(name=name, corpus=corpus, path=path, tagline=tagline, submitter=request.user)
    return character, None


def search(request):
    query = None
    if request.GET:
        query = request.GET.get('q')

    quotemakers = []
    if query:
        quotemakers = watson.filter(Homestarkov, query)
    return render(request, 'search.html', {'user': request.user, 'characters': quotemakers})


@login_required
def delete(request, path):
    character = get_object_or_404(Homestarkov, path=path)
    if request.user != character.submitter:
        raise PermissionDenied
    character.deactivate()
    return redirect('quote:home')


def home(request):
    context = {
        'navbar': 'home',
        'characters': Homestarkov.objects.filter(active=True).all()
    }
    return render(request, 'list.html', context)
