frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

posicao = frase.rfind(caractere) #OLHAR DEPOIS

if posicao == -1:
    print("Caractere não encontrado")
else:
    print("Caractere encontrado na posição", posicao)

    if posicao < 5:
        print("Está no início da frase")
    elif posicao <= 10:
        print("Está no meio da frase")
    else:
        print("Está mais para o final da frase")
