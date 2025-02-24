from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BigAutoField


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = "identifier"

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.id} | {self.image}'