##21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
##BISSEXTO

Ano=int(input("Qual ano você está?"))
if(Ano %4==0):
    print("É bissexto")
else:
    print("Não é bissexto")