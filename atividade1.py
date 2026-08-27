#Atividade 01
nome = input("Qual o seu nome? ")
notaprova1 = int(input("Qual a sua primeira nota? "))
notaprova2 = int(input("Qual a sua segunda nota? "))
media = notaprova1 + notaprova2 / 2
print(f'Sua média é de:{media}')
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    