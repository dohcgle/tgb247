from django.contrib import admin
from .models import Portfolio, ProjectItem

class ProjectItemInline(admin.TabularInline):
    model = ProjectItem
    extra = 1

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('student', 'showcase_url', 'created_at')
    search_fields = ('student__username', 'showcase_url')
    inlines = [ProjectItemInline]

@admin.register(ProjectItem)
class ProjectItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'portfolio', 'skills_demonstrated')
    search_fields = ('title', 'skills_demonstrated')
