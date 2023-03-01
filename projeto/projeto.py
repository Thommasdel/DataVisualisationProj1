"""
Vamos criar um dicionário que contenha como a chave o número do aluno e como valor
tenha uma tupla com a nota das provas feitas ao longo do semestre

O projeto consistirá em:
    -Criar um gráfico de pizza com a porcentagem de alunos aprovados e reprovados
    -Criar um histograma com as médias finais dos alunos
    -Criar um gráfico de colunas mostrando as 3 maiores notas de cada um.

"""
# Imports:
from numpy import*
import random
import matplotlib.pyplot as plt

# Nossos dados:

n_alunos = range(1, 26)

dados = {}

for posicao in n_alunos:
    chave = str(posicao)
    prova = 1
    notas = []
    while prova <= 6:
        nota = random.randrange(0, 11)
        notas.append(nota)
        prova += 1
    dados.update({chave: notas})

print(dados)