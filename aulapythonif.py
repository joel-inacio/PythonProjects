#IF SIMPLES - Possibilidades simples
x = 10

if x == 10:
    print("Bem Vindo")
else:
    print("Adeus")

#IF COMPOSTO - Quando as possibilidades forem maiores do que um
y = 10

if y == 5:
    print("Bem Vindo ao Composto!")
elif y < 20:
    print("Adeus ao Composto")
else:
    print("Saúde ao Composto")

#IF ALINHADO - Quando precisamos saber se mais de um valor ou condição for verdadeira
z = 10
if z == 10 and x < 50 or x < 5:
    if z % 2 == 0:
        if x < 5: #O código para aqui.
            if x < 50:
                print("Oh yeah")

