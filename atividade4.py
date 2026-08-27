#Atividade 04
palavra = input("Digite uma palavra: \n")
minuscula = palavra.lower()
maiuscula = palavra.upper()
tamanho = len(palavra)

print(f'Palavra em minúsculas: {minuscula}')
print(f'Palavra em maiúsculas: {maiuscula}')
print(f'Quantidade de caracteres: {tamanho}')

if tamanho < 5:
    print("Classificação: Palavra curta")
elif 5 <= tamanho <= 8:
    print("Classificação: Palavra média")
else:
    print("Classificação: Palavra longa")
