from django.contrib import admin
from .models import Product, Supplier, Warehouse, Customer, Order, Payment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'brand', 'qty', 'image', 'status', 'timestamp']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'website', 'address', 'timestamp']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'address', 'workercount', 'capacity', 'manager', 'timestamp']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'address', 'status', 'timestamp']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'qty', 'amount', 'order_status', 'timestamp']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'paymentmethod', 'payment_status', 'totalamount', 'timestamp']