from django.db import models
from user.models import MyUser


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(MyUser, on_delete=True)
    posted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:10] + ('..' if len(self.title) > 10 else '')
