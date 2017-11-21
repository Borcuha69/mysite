from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created', 'updated']

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'total_price', 'status', 'created', 'updated']
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'nmb', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'nmb', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)
