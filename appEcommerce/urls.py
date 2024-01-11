from django.urls import path
from .views import index, shop, contact, cart, checkout, productos, create_producto, agregar_al_carrito, ver_carrito, quitar_del_carrito


urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('contact', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('check/', checkout, name='check'),
    path('productos/', productos, name='productos'),
    path('create_producto', create_producto, name='create_producto'),
    path('agregar_al_carrito/<int:id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito', ver_carrito, name="ver_carrito"),
    path('quitar_del_carrito/<int:producto_id>/', quitar_del_carrito, name='quitar_del_carrito')
]
