from django.db import models
# from authentication.models import User

# Create your models here.


class Tag(models.Model):
    class Meta:
        app_label = 'api'
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Link(models.Model):
    # list = models.ManyToManyField(List, related_name='lists', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    image = models.URLField(null=True)
    # tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    links = models.ManyToManyField(Link, related_name='added', blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=250)
    notes = models.TextField(max_length=1000)
    difficulty = models.IntegerField(null=True)



