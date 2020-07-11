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


#função que converte os dados recebidos em dados para exibição conforme esse padrão
def nrzi(entrada):
    controle = 0
    x = []
    for cont in range(len(entrada)):
        if (entrada[cont]==1):
            if (controle == 0):
                x.append(1)
                controle = 1
            else:
                x.append(0)
                controle = 0
        else:
            x.append(controle)
    return x            


  

def nrzi_view(request, entrada):


    entradaDeDados= entrada #exemplo
    entrada_final = entUnicaparavetor(entradaDeDados)
    tamanho = len(entrada_final)

    saida = nrzi(entrada_final)

    y = np.array(saida)
    x = np.arange(0, tamanho, 1)
    plt.step(x, y, where='post')

    plt.xticks(np.arange(0, tamanho, 1.0), (entrada_final))
    plt.yticks(np.arange(0, 2, 1), ('0', '1'))
    plt.grid(True)


    plt.axis([-1,tamanho,-0.1,1.1])

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plt.cla() 
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "nrzi/home.html", {'data': uri, 'entrada': entrada })