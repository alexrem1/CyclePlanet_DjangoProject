from django.contrib import admin
from .models import product, bike_type, brand, deals, condition

# Register your models here.

admin.site.register(product)
admin.site.register(bike_type)
admin.site.register(brand)
admin.site.register(deals)
admin.site.register(condition)