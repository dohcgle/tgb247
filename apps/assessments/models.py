from django.db import models
from apps.courses.models import Module
from apps.accounts.models import User

class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    time_limit_minutes = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Viktorina"
        verbose_name_plural = "Viktorinalar"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    points = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"

class AnswerChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Javob varianti"
        verbose_name_plural = "Javob variantlari"

class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Viktorina urinishi"
        verbose_name_plural = "Viktorina urinishlari"
