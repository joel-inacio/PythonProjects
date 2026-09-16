notas = [10, 7, 6, 5, 5.5, 7.5, 10.5, 9, 5.75, 3, 0]
aprovados = 0
for x in notas:
    if x >= 7.0:
        aprovados +=1
        print("Aprovado!")
        print("Aprovados: ", aprovados)