from django.contrib import admin

from mainapp.models import *


class ItemAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tax, admin.ModelAdmin)
admin.site.register(Discount, admin.ModelAdmin)