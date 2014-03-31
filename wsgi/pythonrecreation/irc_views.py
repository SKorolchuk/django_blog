import os
from django.shortcuts import render_to_response
from django.template import *

def live_chat(request):
    return render_to_response('irc/live_chat.html', dict(user = request.user, is_auth = request.user.is_authenticated()))

