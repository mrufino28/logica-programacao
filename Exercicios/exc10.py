##Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
##mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
##sabendo que cada litro de tinta pinta uma área de 2metros quadrados

L1=float(input("Digite a Largura:"))
A1=float(input("Digite a Altura:"))
AR=L1*A1
print("A área a ser pintada é " + str(AR) + " m²")

TnT=AR/2
print("Tinta necessária para pintar a parede é: "+ str(TnT) + " litros")

