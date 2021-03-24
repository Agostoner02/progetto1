from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import AutoreAL, LibroAL


def homepage(request):
    context = {
        "autori": AutoreAL.objects.all(),
        "libri": LibroAL.objects.all()
    }
    return render(request, "libreria_homepage.html", context)


class LibroListAL(ListView):
    model = LibroAL
    template_name = 'lista_libri.html'
    context_object_name = 'libri'


class LibroDetailAL(DetailView):
    model = LibroAL
    template_name = 'libro_detail.html'
    context_object_name = 'libro'


class AutoreListAL(ListView):
    model = AutoreAL
    template_name = 'lista_autori.html'
    context_object_name = 'autori'


class AutoreDetailAL(DetailView):
    model = AutoreAL
    template_name = 'autore_detail.html'
    context_object_name = 'autore'
