
# Um programa que fala o nome de uma cidade e diz se ela começa ou não com a palavra "Santo"

city = input("Digite uma cidade: \n").lower().strip().split()
print(city[0] == "santo")

#Aqui temos 3 strings fazendo coisas diferentes. São essas: .lower().strip().split()
#Essas strings elas servem para alterar a forma da variável. Ou seja, elas basicamente modificam...
#...Um pouco do conteúdo da variável, para que seja feita a vontade do programador.
#.lower() --> Coloca todos os caracteres em minúsculo
#.strip() -- > Retorna a tradução.. o tipo da string
#.split() --> Se houver, remover espaços que o usuário possa ter colocado na variável. Ex.: " Joel  Joel "
##########################################################################################################
# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

# Faça um programa que leia uma frase qualquer:
frase = str(input("Digite uma frase: \n")).lower().strip()

# Tamanho total da string (quantos caracteres tem a string):
print("Tamanho total da string: {}".format(len(frase))) #Tudo com string

# Quantas vezes aparece a letra "a":
print("A letra A aparece {} vezes na frase.".format(frase.count("a"))) #Tudo com string
#Aqui podemos ver que temos uma "" dentro do parêntesis.. isso quer dizer o que exatamente estamos procurando
#Assim podemos colocar outra letra, que ele fará a mesma coisa com ela.
#O format é o (f'') que podemos usar as {} dentro dos parêntesis.

# Em que posição ela aparece a primeira vez:
print("A primeira letra A aparece na posição {}.".format(frase.find("a"))) #Tudo com string

# Em que posição ela aparece a última vez:
print("A última letra A apareceu na posição {}.".format(frase.rfind("a"))) #Tudo com string
##########################################################################################################
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

nome = "Tertuliano da Silva Moraes Menezes Bueno de Andrada"
nome = nome.split()
print(nome)
print(f"Primeiro = {nome[0]}") #Aqui usamos vetores. No caso o programa vai pegar cada um dos espaços e
#separar em vetores. No caso o vetor 0 é o Tertuliano.
print(f"Último = {nome[-1]}") #Aqui usamos o -1 porque ele pega o último, sem a nescessidade de "contar"
