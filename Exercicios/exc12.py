##12) Crie um programa que leia o preço de um produto, calcule e mostre o seu 
##PREÇO PROMOCIONAL, com 5% de desconto

from time import strftime


P1=float(input("Digite o valor do produto:"))
D=(P1-(P1*5/100))
print("O valor com desconto é: R$"+str(D))