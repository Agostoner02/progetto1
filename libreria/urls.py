from django.urls import path, include
from views import LibroList_AL, AutoreDetail_Al

urlpatterns = [
    path('', LibroList_AL.as_view(), name='lista_libri'),
    path('autore/<int:pk>/ ', AutoreDetail_AL.as_view(), name='profilo_autore')
    
]