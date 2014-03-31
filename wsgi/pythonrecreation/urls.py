from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import os
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', os.environ['OPENSHIFT_APP_NAME'] + '.home_views.home', kwargs=dict(), name='home'),
    url(r'^about/', os.environ['OPENSHIFT_APP_NAME'] + '.home_views.about', kwargs=dict(), name='about'),
    url(r'^irc/chat', os.environ['OPENSHIFT_APP_NAME'] + '.irc_views.live_chat', kwargs=dict(), name='live_chat'),
    url(r'^rss/feed', os.environ['OPENSHIFT_APP_NAME'] + '.rss_views.feed', kwargs=dict(), name='feed'),
    url(r'^login/', os.environ['OPENSHIFT_APP_NAME'] + '.logins_view.login_user', name='auth.control.login'),
    url(r'^profile/', os.environ['OPENSHIFT_APP_NAME'] + '.logins_view.profile', kwargs=dict(), name='profile'),
    url(r'^register/', os.environ['OPENSHIFT_APP_NAME'] + '.logins_view.register', kwargs=dict(), name='register'),
    url(r'^logout/', os.environ['OPENSHIFT_APP_NAME'] + '.logins_view.logout_user', kwargs=dict(), name='logout'),
    # url(r'^pythonrecreation/', include('pythonrecreation.foo.urls')),

    url(r'^forum/forum/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + '.forum_views.forum', kwargs=dict(), name='forum.views.forum'),
    url(r'^forum/thread/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + '.forum_views.thread', kwargs=dict(), name='forum.views.thread'),
    url(r'^forum/post/(new_thread|reply)/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + '.forum_views.post', kwargs=dict(), name='forum.views.post'),
    url(r'^forum/reply/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + '.forum_views.reply', kwargs=dict(), name='forum.views.reply'),
    url(r'^forum/profile/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + '.forum_views.profile', kwargs=dict(), name='forum.views.profile'),
    url(r'^forum/new_thread/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + '.forum_views.new_thread', kwargs=dict(), name='forum.views.new_thread'),
    url(r'^forum/', os.environ['OPENSHIFT_APP_NAME'] + ".forum_views.main", kwargs=dict(), name='forum.views.main'),
    url(r'^news/info/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + ".news_views.news_info", kwargs=dict(), name='news.info'),
    url(r'^news/(\d+)/$', os.environ['OPENSHIFT_APP_NAME'] + ".news_views.news_list", kwargs=dict(), name='news.list.category'),
    url(r'^news/', os.environ['OPENSHIFT_APP_NAME'] + ".news_views.news_list", kwargs=dict(), name='news.list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^data/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
)