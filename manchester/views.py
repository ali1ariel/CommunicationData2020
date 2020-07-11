from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
import io
import urllib, base64



def entUnicaparavetor(entrada):
    x=[]
    for cont in range(len(entrada)):
        if(entrada[cont]=='0'):
            x.append(0)
        else:
            x.append(1)
    return x


# Create your views here.

def desenha_pontos(plt, entrada, passo = 1):
    for cont in range(len(entrada)):
        plt.scatter([cont*passo, ], [entrada[cont], ], 50, color='blue')
    return

def manchester(entrada):
    x = []
    for cont in range(len(entrada)):
        if (entrada[cont]==1):
            x.append(0)
            x.append(1)

        else:
            x.append(1)
            x.append(0)
    return x   
    
    #função auxiliar para ajudar nas informações do gráfico, na reta x
def vetorcontador(entrada):
    x = []
    for cont in range(len(entrada)):
        x.append(cont)
    return x

    

def manchester_view(request, entrada):

    entradaDeDados= entrada #exemplo
    entrada_final = entUnicaparavetor(entradaDeDados)
    tamanho = len(entrada_final)

    saida = manchester(entrada_final)
    tamanho2 = len(saida)
    vetor = vetorcontador(entrada_final)


    y = np.array(saida)
    x = np.arange(0, tamanho2, 1)
    plt.step(x, y, where = 'post')

    plt.xticks(np.arange(0, tamanho2, 2),(entrada_final))
    plt.yticks(np.arange(0, 2, 1), ('0', '1'))
    plt.grid(True)


    plt.axis([-1,tamanho2,-0.1,1.1])

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plt.cla() 
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "manchester/home.html", {'data': uri, 'entrada': entrada })