from django.contrib import admin
from .models import Quiz, Question, AnswerChoice, QuizAttempt

class AnswerChoiceInline(admin.TabularInline):
    model = AnswerChoice
    extra = 4

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'time_limit_minutes')
    list_filter = ('module__subject', 'module')
    search_fields = ('title',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'points')
    list_filter = ('quiz',)
    search_fields = ('text',)
    inlines = [AnswerChoiceInline]

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'score', 'completed_at')
    list_filter = ('completed_at', 'score')
    search_fields = ('student__username', 'quiz__title')
