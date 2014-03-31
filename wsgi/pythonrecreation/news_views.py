import os
from django.shortcuts import render_to_response
from django.template import *
from pythonrecreation.repository.models import *
import sys

def news_list(request):
    news = NewsItem.objects.all()
    categories = NewsCategory.objects.all()
    return render_to_response('news/news_list.html', dict(news_list = news, categories = categories, user = request.user, is_auth = request.user.is_authenticated()))

def news_info(request, pk):
    news_info = NewsItem.objects.get(pk = pk)
    return render_to_response('news/news_info.html', dict(news_info = news_info, user = request.user, is_auth = request.user.is_authenticated()))
