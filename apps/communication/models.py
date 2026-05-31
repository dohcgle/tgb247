from django.db import models
from apps.accounts.models import User
from apps.courses.models import Lesson

class ForumThread(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Forum mavzusi"
        verbose_name_plural = "Forum mavzulari"

class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Forum posti"
        verbose_name_plural = "Forum postlari"
