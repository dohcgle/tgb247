from django.db import models
from apps.courses.models import Lesson
from apps.accounts.models import User

class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_laboratory = models.BooleanField(default=False)
    deadline = models.DateTimeField()

    class Meta:
        verbose_name = "Topshiriq"
        verbose_name_plural = "Topshiriqlar"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    code_snippet = models.TextField(blank=True, null=True)
    file_upload = models.FileField(upload_to='submissions/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Javob (Submission)"
        verbose_name_plural = "Javoblar"
