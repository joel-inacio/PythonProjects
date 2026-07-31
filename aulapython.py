#Primeira aula de programação em Python.
"""
Posso usar essa função das "3 aspas JUNTAS" para comentar um bloco com várias palavras ou com uma explicação
"""

print("Hello World!") #Print é uma função usada para 'falar' alguma coisa na saída do programa. Posso colocar uma variável, ou uma string (texto).
numero = 10 #Aqui temos uma variável com o valor 10. Se eu usar a função print(numero) na saída terei o valor dessa variável
nome = "Joel"
resultado = True
idade = float(18) #Aqui é para mostrar o número com casas decimais, se tiver.

print(nome) #Aqui não podemos colocar uma string (uma frase) junto a uma variável. CONTINUAR LENDO PARA ENTENDER!
print(f'Meu nome é {nome}') #Aqui podemos porque se usa o "f" (f-string) onde permite que eu coloque uma frase junto à variável.
print(f'Meu nome é {nome}, e tenho {idade} anos') #Aqui mostra que posso usar duas ou mais {} nas aspas simples.

print("Vamos nos conhecer melhor!")

nome = input("Digite o seu nome: ") #A função input eu posso usar para colocar a entrada do que o usuário vai escrever no teclado.
idade = int(input("Digite a sua idade: "))
print(f'Prazer em te conhecer! {nome}') #Aqui eu posso colocar as {} para colocar o novo valor que ele editou aqui no INPUT.
print(f'Sua idade é de {idade} anos')

"""
Se formos fazer uma soma matemática onde o usuário deve inserir um valor, devemos sempre colocar o 'int' antes do 'input'
Para que assim o valor não seja 'armazenado' e a soma dê algum erro. Por exemplo:
"""

print("Demonstração de INPUT sem o INT no código")
valor1 = (input("Digite o primeiro valor: "))
valor2 = (input("Digite o segundo valor: "))
soma = valor1 + valor2
print(soma) #Aqui ele não vai somar os valores

print("Demonstração de INPUT com o INT no código")
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))
soma2 = valor3 + valor4
print(soma2) #Aqui ele vai somar, porque o usuário entrou e 'editou' a variável.
