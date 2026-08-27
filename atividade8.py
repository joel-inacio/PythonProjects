primeiro = float(input("Primeiro número: "))
segundo = float(input("Segundo número: "))
operacao = input("Operação: ")

if operacao == "+":
    resultado = primeiro + segundo
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = primeiro - segundo
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = primeiro * segundo
    print("Resultado:", resultado)

elif operacao == "/" and segundo != 0:
    resultado = primeiro / segundo
    print("Resultado:", resultado)

elif operacao == "/" and segundo == 0:
    print("Não é possível dividir por zero")

else:
    print("Operação inválida")
    