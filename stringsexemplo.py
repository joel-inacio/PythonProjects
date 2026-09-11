listadecompras = str(input("\nFaça sua lista de compras: ")).lower().split()
print(f'\n{listadecompras}')

nome = str(input("Digite seu nome: \n")).lower().split()
if "joel" or "fernando" or "silva" in nome:
    print("Nome encontrado")
else:
    print("Nome não encontrado")
