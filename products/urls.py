from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.productslist),
    path('products/<int:pk>/', views.get_products),
]