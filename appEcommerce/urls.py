from django.urls import path
from .views import index, shop, contact, cart, checkout, productos, create_producto

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('contact', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('check/', checkout, name='check'),
    path('productos/', productos, name='productos'),
    path('create_producto', create_producto, name='create_producto')
]