#Atividade 02
idade = int(input("Qual a sua idade? "))
if idade <= 12:
    print("Criança")
elif idade <= 13:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else:
    print("Idoso")
