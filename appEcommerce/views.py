from django.shortcuts import render

from .forms import ProductoForm

from .models import Producto

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

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
        form = ProductoForm(request.POST)
        #si el formulario es valido pasa los datos
        if form.is_valid():
            productoGuardado = Producto(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                stock=form.cleaned_data['stock'],
            )
            productoGuardado.save()
            mensaje='Producto Creado Con Exito'
        else:
            pass
    else:
        form = ProductoForm()
    return render(request, 'registrar_producto.html', {'form': form, 'mensaje':mensaje})