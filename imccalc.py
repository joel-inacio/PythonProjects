#Programa em Python para calcular o IMC (Índice de Massa Corporal)
#imc = peso / (altura ** 2)
#print(imc)

import math

peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite sua altura em METROS: "))

imc = peso / (math.pow(altura,2))

print("Considere apenas os 4 primeiros dígitos. ")
print("Resultado em kg/m² ")
print(math.ceil(imc))
