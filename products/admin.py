from django.contrib import admin
from .models import Product, bike_type, brand, deals, condition

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'SKU',
        'name',
        'brand',
        'price',
        'condition',
        'deals',
        'bike_type',
        'image',
    )

class Bike_typeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class DealsAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(bike_type, Bike_typeAdmin)
admin.site.register(brand, BrandAdmin)
admin.site.register(deals, DealsAdmin)
admin.site.register(condition, ConditionAdmin)