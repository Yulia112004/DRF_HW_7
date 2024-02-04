from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager

NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')

class User(AbstractUser):
    objects = UserManager()
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'