from django.db import models
from apps.accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'TEACHER'})

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

class Module(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Modul"
        verbose_name_plural = "Modullar"

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = CKEditor5Field('Text and Content')
    video_url = models.URLField(blank=True, null=True)
    infographic = models.ImageField(upload_to='infographics/', blank=True, null=True)

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"
