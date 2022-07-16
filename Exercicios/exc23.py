##23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
##para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
##sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo 
##que:
## - Homens ganham 5% de desconto
## - Mulheres ganham 13% de desconto

##import string


from ast import If


Nome=input("Qual seu nome?")
Sexo=int(input("Qual seu sexo? (Digite 1 para Feminino ou 2 para masculino)"))
F=1
M=2
Valor=float(input("Qual o valor gasto:"))

if(Sexo==F):
    desc_mulher=(Valor-(Valor*13/100))
    print("O valor da compra é "+ str(desc_mulher))
else:
    desc_homi=(Valor-(Valor*5/100))
    print("O valor da compra é "+ str(desc_homi))
