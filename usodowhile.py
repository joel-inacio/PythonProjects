x = 0
while x < 5: #O while é como uma instrução que se repete enquanto uma condição for verdadeira
    print(x)
    x = x + 1
#O que acontece:
#O Python checa: "X é maior que 0?" → Não = Executa o bloco.
#Volta a checar: "X é maior que 1?" → Não = Executa de novo.
#Volta a checar: "X é maior que 2?" → Não = Executa de novo.
#Volta a checar: "X é maior que 3?" → Não = Executa de novo.
#Volta a checar: "X é maior que 4?" → Não = Executa de novo.
#Volta a checar: "X é maior que 5?" → Sim = Para.
#No caso aqui ele para pois o valor é maior que cinco
#ELE NUNCA VAI COLOCAR UM VALOR MAIOR DO QUE VOCÊ PEDIU

#Interessante.. para um while "infinito" eu posso declarar: x = 0 e para while x !=9999:

y = 0
while y != 9999:
    y= int(input(" >>>> ")) #Você digita um valor de entrada. Enquanto ele não for = 9999 teremos sempre um loop.