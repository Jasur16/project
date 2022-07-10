from django.contrib import admin
from .models import MessageModel

@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email']