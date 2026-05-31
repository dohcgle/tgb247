from django.db import models
from apps.accounts.models import User

class Portfolio(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    showcase_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfoliolar"

class ProjectItem(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255)
    description = models.TextField()
    artifact = models.FileField(upload_to='portfolio_artifacts/')
    skills_demonstrated = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Loyiha elementi"
        verbose_name_plural = "Loyiha elementlari"
