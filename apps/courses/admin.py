from django.contrib import admin
from .models import Subject, Module, Lesson

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher')
    search_fields = ('title', 'description')
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'order')
    list_filter = ('subject',)
    search_fields = ('title',)
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')
    list_filter = ('module__subject', 'module')
    search_fields = ('title', 'content')
