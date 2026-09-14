from django.shortcuts import render, get_object_or_404
from .models import Producto


def hello_world(request):
    return render(request, "hola.html")


def home(request):
    productos = Producto.objects.filter(
        activo=True
    ).order_by('-fecha_creacion')[:3]

    return render(
        request,
        "app1/home.html",
        {"productos": productos}
    )


def acerca_de_mi(request):
    return render(request, "app1/acerca-de-mi.html")


def catalogo(request):
    productos = Producto.objects.filter(
        activo=True
    ).order_by('-fecha_creacion')

    return render(
        request,
        "app1/catalogo.html",
        {"productos": productos}
    )

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    return render(
        request,
        "app1/detalle.html",
        {"producto": producto}
    )