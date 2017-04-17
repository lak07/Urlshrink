from django.contrib import admin
from f22.models import Post
# Register your models here.
 
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','httpurl')
 
admin.site.register(Post, UrlsAdmin) # Register your models here.
