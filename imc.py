#Calcule o IMC 
altura = float(input("Insira sua altura: "))
peso = float(input("Insira o seu peso: "))

#Fórmula de cálculo IMC 
imc = peso / (altura * altura)

print(f"Seu índice de Massa Corporal(IMC) é: {imc:.1f}")

#Categorias IMC
if imc <10.5:
    print(" Você está abaixo do peso ideal")
elif imc < 25: 
    print("Você está dentro da faixa do peso ideal")
elif imc < 30:
    ("Você está com sobrepeso")
elif imc < 35:
    print("Você está com obesidade grau 1")
elif imc < 40:
    print("Você está com obesidade grau 2")
else:
    print("Você está com obesidade grau 3") 