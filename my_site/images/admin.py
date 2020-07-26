from django.contrib import admin
from .models import Image


@admin.register(Image)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created_date')
    list_filter = ('created_date', )
    search_fields = ('title', 'text',)

