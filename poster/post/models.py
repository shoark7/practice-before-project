from django.db import models
from user.models import User


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    written_time = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    displayed = models.BooleanField(default=True)

    def __str__(self):
        return self.title
