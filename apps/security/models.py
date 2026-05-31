from django.db import models
from apps.accounts.models import User

class AccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    endpoint = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    was_suspicious = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Kirish jurnali"
        verbose_name_plural = "Kirish jurnallari"

class AcademicIntegrityReport(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=100) # e.g., 'PLAGIARISM_SUSPICION', 'TAB_SWITCH_DURING_EXAM'
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Akademik halollik hisoboti"
        verbose_name_plural = "Akademik halollik hisobotlari"
