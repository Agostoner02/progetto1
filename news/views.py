from typing import List
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Articolo, Giornalista


def home(request):
    context = {
        "articoli": Articolo.objects.all(),
        "giornalisti": Giornalista.objects.all()
    }
    return render(request, "homepage.html", context)


class ArticoloListView(ListView):
    model = Articolo
    template_name = 'lista_articoli.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articoli'] = Articolo.objects.all()
        return context


class ArticoloDetailView(DetailView):
    model = Articolo
    template_name = 'articolo_detail.html'


class GiornalistaListView(ListView):
    model = Giornalista
    template_name = 'lista_giornalisti.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['giornalisti'] = Giornalista.objects.all()
        return context


class GiornalistaDetailView(DetailView):
    model = Giornalista
    template_name = 'giornalista_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articoli'] = context['giornalista'].articoli.all()
        return context
