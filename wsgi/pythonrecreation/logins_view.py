from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['is_auth'] = request.user.is_authenticated()
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                c['state'] = state
                c['username'] = username
                return HttpResponseRedirect(reverse("home"))
            else:
                state = "Your account is not active, please contact the site admin."
                c['state'] = state
                c['username'] = username
                return HttpResponseRedirect(reverse("home"))
        else:
            state = "Your username and/or password were incorrect."
    c['state'] = state
    c['username'] = username
    if request.user and request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    else:
        return render_to_response('logins/login.html', c)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

@login_required
def profile(request):
    return render_to_response('logins/profile.html', dict (user = request.user, is_auth = request.user.is_authenticated()))

def register(request):
    state = "Please enter your credentials..."
    username = password = email = ''
    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['is_auth'] = request.user.is_authenticated()
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = True
        user.save()
        state = "You're successfully registered in!"
        c['state'] = state
        c['username'] = username
        c['email'] = email
        return HttpResponseRedirect(reverse("home"))
    c['state'] = state
    c['username'] = username
    return render_to_response('logins/register.html', c)

