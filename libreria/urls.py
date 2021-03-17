from django.urls import path
from .views import homepage, AutoreDetailAL, AutoreListAL, LibroDetailAL, LibroListAL

app_name = 'libreria'
urlpatterns = [
    path('', homepage, name='libreria_home'),
    path('libri/', LibroListAL.as_view(), name='libri_list'),
    path('libri/<int:pk>/', LibroDetailAL.as_view(), name='libro_detail'),
    path('autori/', AutoreListAL.as_view(), name='autori_list'),
    path('autori/<int:pk>/', AutoreDetailAL.as_view(), name='autore_detail'),
]
