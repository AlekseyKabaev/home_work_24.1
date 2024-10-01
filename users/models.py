from django.db import models
from django.contrib.auth.models import AbstractUser

from materials.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to="users/avatars", verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):

    PAYMENT_METHODS = [
        ('cash', 'Наличные '),
        ('transfer_to_account', 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name='Пользователь')
    pay_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    payed_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments', verbose_name='Курс', **NULLABLE)
    payed_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payments', verbose_name='Урок', **NULLABLE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f'{self.user.email} - {self.payment_amount} ({self.pay_date})'
