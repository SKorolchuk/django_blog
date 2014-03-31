import os
from django.shortcuts import render_to_response
from django.template import *

def feed(request):
    return render_to_response('rss/news_feed.html', dict( user =request.user, is_auth = request.user.is_authenticated()))