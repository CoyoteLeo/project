from django.db import models
from user.models import Profile


class Todolist(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, db_index=True)
    title = models.TextField(blank=False)
    content = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    remind_time = models.DateField(blank=True, db_index=True)
    finish_or_not = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.title


class History(models.Model):
    title = models.TextField(blank=False)
    detail = models.TextField(blank=True)
    time = models.DateField(auto_now_add=True)
    version = models.CharField(unique=True, max_length=255, db_index=True)

    def __str__(self):
        return self.title

# Create your models here.
