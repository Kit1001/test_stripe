from django.contrib import admin

from mainapp.models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
