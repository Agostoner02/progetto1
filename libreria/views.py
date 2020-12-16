from .models import Autore, Libro
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class AutoreDetail(DetailView):
    model = Autore
    template_name = "autore.html"


class LibroList(ListView):
    model = Libro
    template_name = "lista_libri.html"