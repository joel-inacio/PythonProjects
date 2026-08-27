frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

frase = frase.lower()
letra = letra.lower()

quantidade = frase.count(letra)

if quantidade == 0:
    print("A letra não aparece na frase")
elif quantidade <= 3:
    print("A letra aparece poucas vezes")
else:
    print("A letra aparece muitas vezes")