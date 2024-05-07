from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('expired', 'Expired'),
    ]
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.completion_date and timezone.now() > self.completion_date:
            self.status = 'expired'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['status']
