from django.shortcuts import render

from .forms import ProductoForm

from django.shortcuts import get_object_or_404, redirect

from .models import Producto, Carrito, ItemCarrito

def index(request):
    return render(request, 'index.html')

def shop(request):
    traer_productos = Producto.objects.all()
    return render(request, 'shop.html', {"productos":traer_productos})

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def productos(request):
    return render(request, 'registrar_producto.html')

def create_producto(request):
    mensaje = None
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        #si el formulario es valido pasa los datos
        if form.is_valid():
            productoGuardado = Producto(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                stock=form.cleaned_data['stock'],
                imagen=form.cleaned_data['imagen']
            )
            productoGuardado.save()
            mensaje='Producto Creado Con Exito'
        else:
            pass
    else:
        form = ProductoForm()
    return render(request, 'registrar_producto.html', {'form': form, 'mensaje':mensaje})



def agregar_al_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    item_carrito, creado = ItemCarrito.objects.get_or_create(producto=producto)
    if item_carrito in carrito.items.all():
        item_carrito.cantidad += 1
        item_carrito.save()
    else:
        carrito.items.add(item_carrito)

    return redirect('ver_carrito')

def quitar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito = Carrito.objects.get(usuario=request.user)

    item_carrito = get_object_or_404(ItemCarrito, producto=producto)
    item_carrito.cantidad -= 1
    item_carrito.save()

    if item_carrito.cantidad == 0:
        carrito.items.remove(item_carrito)

    return redirect('ver_carrito')

def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})