frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para pesquisar: ")

palavras = frase.lower().split()
palavra = palavra.lower()

if palavra in palavras:
    print("Palavra encontrada")
else:
    print("Palavra não encontrada")