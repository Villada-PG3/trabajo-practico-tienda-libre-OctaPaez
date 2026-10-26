from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto


class HomeView(TemplateView):
    template_name = "app1/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["productos"] = Producto.objects.filter(
            activo=True
        ).order_by("-fecha_creacion")[:3]

        return context


class CatalogoView(ListView):
    model = Producto
    template_name = "app1/catalogo.html"
    context_object_name = "productos"
    paginate_by = 6

    def get_queryset(self):
        return Producto.objects.filter(
            activo=True
        ).order_by("-fecha_creacion")


class DetalleProductoView(DetailView):
    model = Producto
    template_name = "app1/detalle.html"
    context_object_name = "producto"


def acerca_de_mi(request):
    return render(request, "app1/acerca-de-mi.html")