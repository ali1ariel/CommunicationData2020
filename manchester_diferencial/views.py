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

def diffmanchester(entrada):
    estado = True
    x = []
    for cont in range(len(entrada)):
        if(entrada[cont]==0):
            if (estado == True):
                x.append(0)
                x.append(1)
            else:
                x.append(1)
                x.append(0)
        else:
            if (estado == True):
                x.append(1)
                x.append(0)
                estado = False

            else:
                x.append(0)
                x.append(1)
                estado = True
    return x
        
    
    
    
def vetorcontador(entrada):
    x = []
    for cont in range(len(entrada)):
        x.append(cont)
    return x
    
    

def manchester_diferencial_view(request, entrada):


    entradaDeDados= entrada #exemplo
    entrada_final = entUnicaparavetor(entradaDeDados)
    tamanho = len(entrada_final)

    saida = diffmanchester(entrada_final)
    saida.insert(0, 1)
    tamanho2 = len(saida)
    vetor = vetorcontador(entrada_final)


    y = np.array(saida)
    x = np.arange(0, tamanho2, 1)
    #decide o gráfico de passos, where = pre significa que a linha muda antes do dado.
    plt.step(x, y, where = 'pre')

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
    return render(request, "manchester_diferencial/home.html", {'data': uri, 'entrada': entrada })