from .models import Autore, Libro
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class AutoreDetail_AL(DetailView):
    model = Autore
    template_name = "autore.html"


class LibroList_AL(ListWiew):
    model = Libro
    template_name = "lista_libri.html"