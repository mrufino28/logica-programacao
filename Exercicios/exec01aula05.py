##Descobrir qual a idade

from cgi import print_arguments


Ano_atual=int(input("Qual ano estamos?"))
Ano_nasc=int(input("Qual ano vocÊ nasceu?"))
Idade=Ano_atual-Ano_nasc
print ("Sua idade é "+ str(Idade))

Reais=float(input("Quantos R$ você possui?"))
Dolar=Reais/2.22
print("Então você possui "+str(Dolar))