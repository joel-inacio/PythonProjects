"""
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
"""
"""
#Atividade 02
idade = int(input("Qual a sua idade? "))
if idade <= 12:
    print("Criança")
elif idade <= 13:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
"""
"""
#Atividade 03
usuario = input("Nome de Usuário: ").lower()
senha = int(input("Senha: "))
adminusuario = "admin"
senhausuario = 1234
if usuario == adminusuario and senha == senhausuario:
    print("Login Realizado com Sucesso")
else:
    print("Usuário ou senha incorretos")
"""
#Atividade 04
palavra = str(input("Digite uma palavra: \n")).upper().lower().split()
print(palavra)
