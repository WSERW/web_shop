from django.contrib import admin
from .models import Order, OrderItem, CallRequest

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone','delivery_way',
                    'address', 'city', 'paid', 'comment',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
class CallRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone',
                    'created', 'updated']
    list_filter = ['name', 'created', 'updated']

admin.site.register(CallRequest, CallRequestAdmin)
