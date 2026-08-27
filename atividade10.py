frase = input("Digite uma frase: ")

print("Maiúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Quantidade de caracteres:", len(frase))

palavras = frase.split()
print("Palavras:", palavras)

quantidade_a = frase.lower().count("a")
print("Quantidade de letras 'a':", quantidade_a)

posicao_a = frase.lower().rfind("a")
print("Posição da última letra 'a':", posicao_a)

if len(frase) < 20:
    print("Frase curta")
elif len(frase) <= 50:
    print("Frase média")
else:
    print("Frase longa")

if quantidade_a > 0 and quantidade_a > 3:
    print("A frase possui a letra 'a' e ela aparece mais de 3 vezes")
else:
    print("A frase não possui mais de 3 ocorrências da letra 'a'")