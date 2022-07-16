#27) Crie um programa que leia duas notas de um aluno e calcule a sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
 #- Média 7.0 ou superior: APROVADO

from tkinter.tix import InputOnly


Nota1=float(input("DIgite a primeira nota: "))
Nota2=float(input("Digite a segunda nota: "))
M=(Nota1+Nota2)/2
if(M<=4.9):
   print("REPROVADO")
if(5.0<M<6.9):
    print("RECUPERAÇÃO")
if(M>7):
    print("APROVADO")