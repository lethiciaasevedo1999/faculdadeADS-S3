import random

lista_opcoes = ['A', 'B', 'C', 'D', 'E']

escolha_aleatoria = random.choice(lista_opcoes)
print(escolha_aleatoria)

#embaralhar a lista com Shuffle
random.shuffle(lista_opcoes)
print(lista_opcoes)