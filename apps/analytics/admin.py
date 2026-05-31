from django.contrib import admin
from .models import UserActivity, PerformanceMetric

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_type', 'timestamp')
    list_filter = ('action_type', 'timestamp')
    search_fields = ('user__username', 'action_type')

@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ('student', 'average_quiz_score', 'assignments_completed', 'calculated_at')
    list_filter = ('calculated_at',)
    search_fields = ('student__username',)
