from django.db import models
from apps.accounts.models import User

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100) # e.g., 'LESSON_VIEW', 'LOGIN'
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foydalanuvchi faolligi"
        verbose_name_plural = "Foydalanuvchi faolliklari"

class PerformanceMetric(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    average_quiz_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    assignments_completed = models.PositiveIntegerField(default=0)
    calculated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Samaradorlik ko'rsatkichi"
        verbose_name_plural = "Samaradorlik ko'rsatkichlari"
