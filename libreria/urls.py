from django.urls import path, include
from views import LibroList, AutoreDetail

urlpatterns = [
    path('', LibroList.as_view(), name='lista_libri'),
    path('autore/<int:pk>/ ', AutoreDetail.as_view(), name='profilo_autore')
    
]