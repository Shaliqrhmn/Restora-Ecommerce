from django.urls import path
from . import views
app_name = 'cartapp'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('delete/<int:product_id>/', views.cart_remove, name='delete_from_cart'),
    path('delete_all/<int:product_id>/', views.delete_all, name='delete_all')
]
