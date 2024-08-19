#Lista que contém os quadrados dos números de 1 a 10

quadrados = []

for num in range(1,11):
    quadrados.append(num ** 2)

print(quadrados)

#Outra forma
quadrados = [num **2 for num in range(1,11)]
print(quadrados)
