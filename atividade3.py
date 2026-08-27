#Desafio: faça a comparação do usuário sem diferenciar letras maiúsculas e
#minúsculas utilizando .lower().

usuario = input("Nome de Usuário: ").lower()
senha = int(input("Senha: "))
adminusuario = "admin"
senhausuario = 1234
if usuario == adminusuario and senha == senhausuario:
    print("Login Realizado com Sucesso")
else:
    print("Usuário ou senha incorretos")
