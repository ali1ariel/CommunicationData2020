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



entradaDeDados='011101101'#exemplo
entrada = entUnicaparavetor(entradaDeDados)
tamanho = len(entrada)

# Create your views here.

def desenha_pontos(plt, entrada, passo = 1):
    for cont in range(len(entrada)):
        plt.scatter([cont*passo, ], [entrada[cont], ], 50, color='blue')
    return

def nrzl(entrada):
    x=[]
    for cont in range(len(entrada)):
        if(entrada[cont]==1):
            x.append(0)
        else:
            x.append(1)
    return x

    

def nrzl_view(request, entrada):


    entradaDeDados= entrada #exemplo
    entrada_final = entUnicaparavetor(entradaDeDados)
    tamanho = len(entrada)


    saida = nrzl(entrada_final)
    y = np.array(saida)
    x = np.arange(0, tamanho, 1)

    #definem as proporções do gráfico para as linhas de fundo
    #xticks vai x de 0 ao tamanho do vetor, sendo 1 de distancia.
    #yticks o mesmo, de 0 a 2, e 1 a distancia.
    plt.xticks(np.arange(0, tamanho+1, 1),(entrada_final))
    plt.yticks(np.arange(0, 2, 0.5),('','0'))
    #desenha as linhas do gráfico
    plt.grid(True)

    #decide o gráfico de passos, where = post significa que a linha só muda no próximo dado.
    plt.step(x, y, where='post')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plt.cla() 
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "nrzl/home.html", {'data': uri, 'entrada': entrada })