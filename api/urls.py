from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_view),
    path('products/', views.product_view),
    path('orders/', views.order_view),
]