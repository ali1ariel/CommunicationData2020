from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import EntradaForm
import json


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            print("OKAY!")
    else:
        form = EntradaForm()


    return render(request, "base/entrada.html", {'form': form })

def set_entrada(request):
    entrada = request.POST['entrada']
    return redirect('ami', entrada=entrada)

