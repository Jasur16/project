from django.contrib import admin

from .models import AboutModel, MessageModel
from modeltranslation.admin import TranslationAdmin

@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['created_at']

@admin.register(AboutModel)
class AboutModelAdmin(TranslationAdmin):
    list_display = ['id']
    list_display_links = ['id']


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

