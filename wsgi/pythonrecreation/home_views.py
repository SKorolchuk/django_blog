import os
from django.shortcuts import render_to_response
from django.template import *
from pythonrecreation.repository.models import *
import sys

def home(request):
    return render_to_response('home/home.html', dict(user = request.user, is_auth = request.user.is_authenticated()))

def about(request):
    return render_to_response('home/about.html', dict(user = request.user, is_auth = request.user.is_authenticated()))

