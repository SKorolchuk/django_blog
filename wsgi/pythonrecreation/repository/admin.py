from django.contrib import admin
from pythonrecreation.repository.models import *

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        (None, {'fields': ['pub_date']}),
    ]

admin.site.register(Poll, PollAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(Photo, PhotoAdmin)