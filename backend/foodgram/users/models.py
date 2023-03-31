from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Subscriptions(models.Model):
    """Подписка"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор', related_name='following'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='follow'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
