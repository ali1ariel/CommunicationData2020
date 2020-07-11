from django import forms

class EntradaForm(forms.Form):
    entrada = forms.CharField(label="Digite a entrada de dados", max_length=20)
