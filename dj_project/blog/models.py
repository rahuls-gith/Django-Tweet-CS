from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    post = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)    # auto_now=True (can be used for last modified); auto_now_add=True (can be used here but we won't be able to change this data in future)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if a user is deleted, then delete the corresponding many posts (1-to-many relationship) using CASCADE

    def __str__(self):
        return self.title   