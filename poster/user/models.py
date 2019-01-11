from django.db import models
from django.contrib.auth.models import User as DEFAULT_USER


class User(models.Model):
    user = models.OneToOneField(DEFAULT_USER, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    profile_image = models.ImageField()
    get_email = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
