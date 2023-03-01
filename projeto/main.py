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
import funcoes

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

medias_alunos = {chave: funcoes.calcula_media(valor) for chave, valor in dados.items()}

# Gráfico de colunas mostrando as 3 maiores notas de cada aluno

x = arange(len(n_alunos))
largura = 0.3 # Largura das colunas

notas_1 = funcoes.pega_nota(dados, 1)
notas_2 = funcoes.pega_nota(dados, 2)
notas_3 = funcoes.pega_nota(dados, 3)

grafico1 = plt.bar(x - 3*largura/2, notas_1, width=largura, label="1ª Maior Nota", align="edge")
grafico2 = plt.bar(x, notas_2, width=largura, label="2ª Maior Nota", align="center")
grafico3 = plt.bar(x + largura/2, notas_3, width=largura, label="3ª Maior Nota", align='edge')

plt.xlabel("Alunos")
plt.title("Maiores notas por aluno")
plt.xticks(x, dados.keys())
plt.legend()

funcoes.legenda_automatica(grafico1)
funcoes.legenda_automatica(grafico2)
funcoes.legenda_automatica(grafico3)


plt.show()

# Histograma com as médias finais

plt.hist(medias_alunos.values(), bins=25, align='mid', histtype='barstacked', 
        color='cyan', label='Médias finais' )

plt.legend()
plt.xlabel("Médias")
plt.ylabel("Número de alunos")
plt.title("Médias gerais")
plt.show()
