from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormContatto
from django.contrib.auth.decorators import login_required

@login_required
def contatti(request):

    if request.method == "POST":
        form = FormContatto(request.POST)

        if form.is_valid():
            nuovo_contatto = form.save()
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            return HttpResponse("<h1>Grazie per averci contattato</h1>")

    form = FormContatto()
    context = {"form": form}
    return render(request, "contatto.html", context)
