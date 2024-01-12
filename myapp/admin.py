from django.contrib import admin

# Register your models here.
from .models import PostName, Post, Message


admin.site.register(PostName)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','publish','created','auther','postname']
    list_filter=['title','auther']
    search_fields=['title','body', 'auther']
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=['Mbody','post']

