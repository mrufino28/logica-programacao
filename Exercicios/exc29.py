#29) Desenvolva um programa que leia o nome de um funcionário, seu salário, 
#quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de 
#acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%

from tkinter.tix import InputOnly


Nome=input("Digite o nome do funcionário: ")
Salario=int(input("Digite o salário do funcionário: "))
Anos=int(input("Quantos anos de empresa o funcionário possui: "))
if(Anos<=3):
    print("O novo salário é:" + str(Salario+(Salario*3/100)))
if(3<Anos<=10):
     print("O novo salário é:" + str(Salario+(Salario*12.5/100)))
if(Anos>10):
    print("O novo salário é:" + str(Salario+(Salario*20/100)))