import matplotlib.pyplot as plt
from numpy import*
import random

# Calculando a média dos alunos: A média será formada pelas 3 maiores médias obtidas pelos alunos

def ordena_notas(listagem): #Função para ordenar as notas em ordem decrescente
    ordenadas = sorted(listagem, reverse=True)
    return ordenadas

def calcula_media(listagem): #A função calcula a média dos 3 maiores notas obtidas
    lista_ordenada = ordena_notas(listagem)
    pos = 0
    soma = 0
    while pos < 3:
        soma += lista_ordenada[pos]
        pos += 1
    return round(soma/3, 2) #Função round() arredonda os vaalores decimais


def pega_nota(dicionario, posicao_nota):
    """Função que recebe um dicionário cujos valores são um iterável com as notas
        dos alunos e recebe a posição da nota desejada (Maior nota, 2' maior nota, etc)
    """

    lista = []
    valores = dicionario.values()
    for i in valores:
        maior_nota = ordena_notas(i)[posicao_nota]
        lista.append(maior_nota)
    return lista

def legenda_automatica(grafico):
    for i in grafico:
        altura = i.get_height()
        plt.annotate(f'{altura}', xy=(i.get_x() + i.get_width()/2, altura),
                     xytext=(0, 2), textcoords="offset points", ha='center')

