from django.contrib import admin
from links.models import Link


class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

admin.site.register(Link, LinkAdmin)
