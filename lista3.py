#Fatiando uma lista

nomes = ['Lethicia', 'Fernando', 'Kevin', 'Lucas', 'Nihao']

nomes_fatiar = nomes[:2]
#print(nomes_fatiar)

#Copiando uma lista 
copiar_nomes = nomes[:]
#print(copiar_nomes)

#Adicionando nomes na lista por concatenação
minha_lista = []
lista_itens = ['Lethicia', 'Fernando', 'Kevin']

minha_lista += lista_itens
#print(minha_lista)

#Método extends
minha_lista = []
lista_itens = ['Lethicia', 'Fernando', 'Kevin']
minha_lista.extend(lista_itens)
print(minha_lista)