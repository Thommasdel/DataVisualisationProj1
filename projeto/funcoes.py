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

