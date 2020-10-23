from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<product_id>', views.product_detail, name="product_detail"),
    path('bike_type_landing/', views.bike_type_landing, name="bike_type_landing"),
    path('condition_landing/', views.condition_landing, name="condition_landing"),
    path('brand_landing/', views.brand_landing, name="brand_landing"),
]
