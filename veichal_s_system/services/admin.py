from django.contrib import admin
from .models import Component, Vehicle, Issue, Transaction

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'repair_price', 'new_price', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_id', 'owner_name', 'model', 'created_at')
    search_fields = ('vehicle_id', 'owner_name', 'model')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'description', 'component', 'is_new_component', 'created_at')
    search_fields = ('vehicle__vehicle_id', 'description', 'component__name')
    list_filter = ('is_new_component', 'created_at')
    ordering = ('-created_at',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'total_price', 'paid', 'created_at')
    search_fields = ('vehicle__vehicle_id',)
    list_filter = ('paid', 'created_at')
    ordering = ('-created_at',)
