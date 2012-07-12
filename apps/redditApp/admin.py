import redditApp.models
from django.contrib import admin


class LinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,     {"fields": ["description", "link", "sub_by", ]}),
        (None,     {"fields": ["sub_date", "points"]}),
    ]
    list_display = ("description", "sub_date", "points")
    search_fields = ["description", "link"]
admin.site.register(redditApp.models.Link, LinkAdmin,)


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {"fields": ["link", ]}),
        (None,  {"fields": ["comment", "author", "date", "points"]}),
    ]
    list_display = ("comment", "date", "points")
    search_fields = ["links", "comment", "author"]
admin.site.register(redditApp.models.Comment, CommentAdmin,)
