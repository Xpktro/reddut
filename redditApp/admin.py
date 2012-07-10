from redditApp.models import Link
from django.contrib import admin

class LinkAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None,     {"fields": ["description", "link",]}),
                 (None,     {"fields": ["sub_date", "points"]}),
    ]
    list_display = ("description", "sub_date", "points")
    search_fields = ["description", "link"]

admin.site.register(Link, LinkAdmin)