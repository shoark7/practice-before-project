from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User
)

class MyUserManager(BaseUserManager):
    def create_user(self, user_identifier, nickname, image=None, password=None):
        if not user_identifier:
            raise ValueError("Users must have IDs")

        user = self.model(
            user_identifier=user_identifier,
            nickname=nickname,
            user_image=image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_identifier, nickname, password):
        user = self.create_user(
            user_identifier=user_identifier,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    user_identifier = models.CharField('ID', max_length=20, unique=True)
    user_image = models.ImageField(upload_to='user_image/', blank=True, null=True)
    nickname = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'user_identifier'
    REQUIRED_FIELDS = ['nickname']


    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
