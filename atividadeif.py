"""
# ATIVIDADE 01
x = 10
y = 30
if y > x:
        print("Maior")
else:
        print("Menor")

"""

"""
# ATIVIDADE 02
pnome = input("Digite o primeiro nome: ")
peso = input("Digite o primeiro peso: ")

pnome2 = input("Digite o segundo nome: ")
peso2 = input("Digite o segundo peso: ")

if peso > peso2:
    print(f'A pessoa mais pesada é {pnome}, que pesa {peso} kg.')
elif peso2 > peso:
    print(f'A pessoa mais pesada é {pnome2}, que pesa {peso2} kg.')
else:
    print(f'Ambos têm o mesmo peso! {pnome} e {pnome2} pesam {peso} kg.')
"""

"""
# ATIVIDADE 03
anoatual = 2026
inome = input("Digite seu nome: ")
anonascimento = int(input("Digite seu ano de nascimento: "))

inome2 = input("Digite seu nome: ")
anonascimento2 = int(input("Digite seu ano de nascimento: "))

resultado = anoatual - anonascimento
resultado2 = anoatual - anonascimento2
print(f'O {inome} tem {resultado} anos!')
print(f'O {inome2} tem {resultado2} anos!')

if resultado2 > resultado:
    print(f'O {inome} tem {resultado} e é o mais novo')
elif resultado2 < resultado:
    print(f'O {inome2} tem {resultado2} e é o mais novo')
else:
    print(f'Ambos tem a mesma idade! {resultado2} anos.')
"""

#ATIVIDADE 05
metajorge = 1000
vendasjorge = 0
usuario = 151515
senha = 123456
print("Bem-vindo ao Supermercado Compre Mais!")
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
if usuario == usuario and senha == senha:
    print("\nBem-vindo ao Supermercado Compre Mais!")
    print(f'Usuário: {usuario}')
else:
    print("Acesso Negado")

vendasjorge = input("Digite o valor da nova venda realizada: ")
if vendasjorge > metajorge:
    print("Ganhou!")
else:
    print("Continue vendendo!")
