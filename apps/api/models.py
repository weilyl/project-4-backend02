from django.db import models
from authentication.models import User

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    list = models.ForeignKey(List, related_name='lists')
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

