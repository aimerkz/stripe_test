from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField('Название', max_length=99)
    description = models.CharField('Описание', max_length=99)
    price = models.PositiveIntegerField(
        'Цена',
        default=0
    )

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ('-id', )

    def __str__(self):
        return f'{self.name} -- {self.price}'


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='items')
    name = models.CharField(max_length=49, default='')
    total_sum = models.PositiveIntegerField(
        'Итоговая стоимость',
        default=0
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-id', )
