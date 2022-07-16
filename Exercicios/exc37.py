#37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um 
#aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, 
#o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. 
#No final, mostre o seu novo salário, baseado na tabela a seguir:
#- Mulheres
# - menos de 15 anos de empresa: +5%
#- de 15 até 20 anos de empresa: +12%
#- mais de 20 anos de empresa: +23%
#- Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

S=float(input("Qual o salário atual: "))
F=int(input("Qual o gênero do Funcionário: (Digite 1 para Feminino e 2 para Masculino"))
Anos=int(input("Quantos anos de empresa: "))

if(F==1):
    if(Anos<15):
        print("O novo salário é "+ str(S+(S*5/100)))
    if(15<Anos<=20):
         print("O novo salário é "+ str(S+(S*12/100)))
    if(Anos>20):
         print("O novo salário é "+ str(S+(S*25/100)))
if(F==2):
    if(Anos<20):
        print("O novo salário é "+ str(S+(S*3/100)))
    if(20<Anos<=30):
         print("O novo salário é "+ str(S+(S*13/100)))
    if(Anos>30):
         print("O novo salário é "+ str(S+(S*25/100)))
