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

def pseudoternario(entrada):
    controle = 0
    posicao = 0
    subindo = False
    x = []
    for cont in range(len(entrada)):
        if(cont==0):
            if(entrada[cont]==0):
                x.append(1)
                posicao = 1
                controle = 0
            else:
                x.append(-1)
                posicao = -1
                controle = 1
                subindo = True
        elif(entrada[cont]==controle):
            if(posicao==-1):
                x.append(1)
                posicao=1
                subindo = False
            elif(posicao==1):
                x.append(-1)
                posicao=-1
                subindo = True
            else:
                x.append(0)
                posicao=0
        else:
            if(subindo == True and posicao != 1):
                x.append(posicao+1)
                
            if(subindo == False and posicao != -1):
                x.append(posicao-1)
    return x
            

    

    

def pseudoternario_view(request, entrada):


    entradaDeDados= entrada #exemplo
    entrada_final = entUnicaparavetor(entradaDeDados)
    tamanho = len(entrada_final)
    
    saida = pseudoternario(entrada_final)

    y = np.array(saida)
    x = np.arange(0, tamanho, 1)
    plt.step(x, y, where = 'post')

    plt.xticks(np.arange(0, tamanho+1, 1),(entrada_final))
    plt.yticks(np.arange(-1, 3, 1), ('-', '0', '+'))
    plt.grid(True)


    plt.axis([-1,tamanho,-1.1,1.1])

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plt.cla() 
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "pseudoternario/home.html", {'data': uri, 'entrada': entrada })