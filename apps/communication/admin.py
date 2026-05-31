from django.contrib import admin
from .models import ForumThread, ForumPost

class ForumPostInline(admin.TabularInline):
    model = ForumPost
    extra = 1

@admin.register(ForumThread)
class ForumThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'lesson', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__username')
    inlines = [ForumPostInline]

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'author', 'created_at')
    search_fields = ('content', 'author__username')
