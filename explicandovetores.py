#Listas
alunos = ["Joel", "Ronaldo", "Maria"]
numeros = [16,27,31,49,52,60] #Lista de alunos, com seus números sendo a identificação dos mesmos.
#print(numeros[0]) #Printar na tela o aluno com índice zero, no caso é o primeiro.
#print(alunos[-1]) #Printar na tela o nome dos alunos com o índice -1 que no caso é o último da lista.
#Para ficar mais "fácil" pode-se apenas subtrair um número, para saber o índice dele. No caso, se eu quero o 5, o índice é 5-1 = 4
numeros[1] = 280 #Aqui podemos editar um elemento da lista, que é correspondente ao vetor. Valor no vetor 1 vai valer agora 280
print(numeros)
alunos.append(650)
alunos.insert(2,1000) #Aqui serve para INSERIR um valor, ou string na lista
alunos.remove("Joel") #Aqui serve para REMOVER um valor, ou string na lista
alunos.pop(1) #Aqui serve para REMOVER um valor, ou string na lista por meio do ÍNDICE dele
#Função para adicionar uma variável, número ou string no FINAL da minha variável.
print(alunos)
for x in numeros:
    if x % 2 == 0:
        print(f"Número par {x}")
    else:
        print(f"Número ímpar {x}")
print("\n...............................................")
listaalunos = ["Ana", "Carlos", "João"]
print("Ana" in listaalunos)
if "Ana" in listaalunos:
    print("Ana está presente")
else:
    print("Ana não está presente")

