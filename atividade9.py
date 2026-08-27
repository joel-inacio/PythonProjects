nome = input("Nome do usuário: ")
idade = int(input("Idade: "))
tipo = input("Tipo de usuário: ")

tipo = tipo.lower()

if tipo == "admin":
    print(nome, "- acesso total")

elif tipo == "professor" and idade >= 18:
    print(nome, "- acesso ao sistema acadêmico")

elif tipo == "aluno" and idade >= 16:
    print(nome, "- acesso à área do aluno")

else:
    print(nome, "- acesso negado")