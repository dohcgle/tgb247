from django.contrib import admin
from .models import AccessLog, AcademicIntegrityReport

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'endpoint', 'timestamp', 'was_suspicious')
    list_filter = ('was_suspicious', 'timestamp')
    search_fields = ('ip_address', 'endpoint', 'user__username')

@admin.register(AcademicIntegrityReport)
class AcademicIntegrityReportAdmin(admin.ModelAdmin):
    list_display = ('student', 'incident_type', 'reported_at')
    list_filter = ('incident_type', 'reported_at')
    search_fields = ('student__username', 'description')
