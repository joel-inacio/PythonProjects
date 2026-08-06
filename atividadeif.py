"""
OPERADORES MATEMÁTICOS

+ (Adição): Soma dois valores (ex: 5 + 3 resulta em 8).
- (Subtração): Subtrai o segundo valor do primeiro (ex: 5 - 3 resulta em 2).
* (Multiplicação): Multiplica dois valores (ex: 5 * 3 resulta em 15).
/ (Divisão): Divide o primeiro valor pelo segundo, retornando sempre um número de ponto flutuante (float) (ex: 7 / 2 resulta em 3.5).
// (Divisão Inteira): Divide e descarta a parte decimal, arredondando para baixo (ex: 7 // 2 resulta em 3).
% (Módulo ou Resto da Divisão): Retorna o resto da divisão inteira (ex: 7 % 2 resulta em 1).
** (Exponenciação ou Potenciação): Eleva o primeiro valor à potência do segundo (ex: 2 ** 3 resulta em 8)

OPERADORES DE COMPARAÇÃO
== (Igual a): Verifica se dois valores são iguais.
!= (Diferente de): Verifica se dois valores são diferentes.
> (Maior que): Verifica se o valor à esquerda é maior que o da direita.
< (Menor que): Verifica se o valor à esquerda é menor que o da direita.
>= (Maior ou igual a): Verifica se o valor à esquerda é maior ou igual ao da direita.
<= (Menor ou igual a): Verifica se o valor à esquerda é menor ou igual ao da direita
"""
#print("\nQuestões Resolvidas do: IF e ELSE")
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
#ATIVIDADE 04
valor = int(input("\nDigite um número: "))
print(f'O número escolhido foi o {valor}')
if valor % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")

"""
#ATIVIDADE 05
import sys

metajorge = 1000
vendasjorge = 0
usuario = 600603
senha = 123456
print("\nBem-vindo ao Supermercado Compre Mais!")
entradausuario = int(input("\nDigite seu usuário: "))
entradasenha = int(input("Digite sua senha: "))
if usuario == entradausuario and senha == entradasenha:
    print("\nBem-vindo ao Supermercado Compre Mais!")
    print(f'Usuário: {usuario}')
else:
    print("Acesso Negado")
    sys.exit()

vendasjorge = int(input("Digite o valor da nova venda realizada: "))
if vendasjorge > metajorge:
    print("Você foi além e atingiu sua meta! Ganhou!")
elif vendasjorge < metajorge:
    print("Continue vendendo")
else:
    print("Você atingiu exatamente sua meta! Ganhou!")
"""
