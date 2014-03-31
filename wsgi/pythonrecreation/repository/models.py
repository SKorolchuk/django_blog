import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db   import models
from django.utils import timezone
from django.contrib import admin
from django.db.models.signals import post_save

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pic_folder/')
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1024)
    image = models.ForeignKey(Photo)

    def __unicode__(self):
        return self.title

    def num_posts(self):
        return sum([t.num_posts() for t in self.thread_set.all()])

    def last_post(self):
        if self.thread_set.count():
            last = None
            for t in self.thread_set.all():
                l = t.last_post()
                if l:
                    if not last or l.created > last.created:
                        last = l
            return last


class Thread(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)
    description = models.TextField(max_length=1024)

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return self.post_set.count() - 1

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]


class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField(max_length=10000)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.thread, self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))
    short.allow_tags = True

    def profile_data(self):
        if self.creator.userprofile_set.all():
            p = self.creator.userprofile_set.all()[0]
            return p.posts, p.avatar


class UserProfile(models.Model):
    avatar = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
    posts = models.IntegerField(default=0)
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return unicode(self.user)

class NewsCategory(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    short_info = models.TextField(max_length=1024)
    image = models.ForeignKey(Photo)

class NewsItem(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    category = models.ForeignKey(NewsCategory)
    body = models.TextField(max_length=32768)
    short_info = models.TextField(max_length=1024)
    image = models.ForeignKey(Photo)

### Admin

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]

class ForumAdmin(admin.ModelAdmin):
    pass

class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "thread", "creator", "created"]

class PhotoAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "image", "creator", "created"]

class NewsItemAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "category", "creator", "created", "body", "short_info", "image"]

class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "creator", "created", "short_info", "image"]

def create_user_profile(sender, **kwargs):
    """When creating a new user, make a profile for him."""
    u = kwargs["instance"]
    if not UserProfile.objects.filter(user=u):
        UserProfile(user=u).save()

post_save.connect(create_user_profile, sender=User)
