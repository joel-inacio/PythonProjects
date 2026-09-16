 #O for é como uma instrução repetida para cada item de uma lista.
nomes = ["Ana", "Bruno", "Carla"]

for nome in nomes:
    print("Olá, " + nome) #Executa o print para todos os itens da lista, e não para apenas um em específico.
#Agora, caso eu não tenha essa lista mas eu quero usar o for para repetição, uso a função .range()
for i in range(3):
    print("Pule!") #Isso imprime "Pule!" três vezes. O range(3) é só uma forma de dizer "me dá 3 repetições".
#for = "para cada item, faça isso".
#.range() = "faça tal coisa, em uma quantidade x de vezes"
