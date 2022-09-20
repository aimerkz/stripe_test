from django.contrib import admin
from api.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    empty_value_display = 'empty'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('items', 'name')
    list_display = ('id', 'name', 'total_sum')
    empty_value_display = 'empty'
