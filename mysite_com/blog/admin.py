from django.contrib import admin
from blog.models import Entry
from tinymce.widgets import TinyMCE
from django import forms


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title', 'pub_date', 'status')
    list_filter = ('status',)
    #list_filter = ('get_status_display')

    class Media:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js',)

admin.site.register(Entry, EntryAdmin)
