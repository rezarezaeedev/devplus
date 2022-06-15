from django.contrib import admin
from .models import SiteInfo


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display= ['id','title','admin_name','is_active']
    list_display_links = list_display

