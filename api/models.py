from django.db import models
from django.dispatch import receiver
from django.db.models.signals import m2m_changed


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


@receiver(m2m_changed, sender=Order.items.through)
def total_sum(sender, instance, action, **kwargs):
    """Method to automatically calculate the total cost of all Items"""
    if action == 'post_add':
        total_sum = 0
        for item in instance.items.all():
            total_sum += item.price
        instance.total_sum = total_sum
        instance.save()
