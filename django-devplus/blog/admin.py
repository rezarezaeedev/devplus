from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ['id','title','author','is_active']
    list_display_links = list_display

