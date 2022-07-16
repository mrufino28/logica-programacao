#26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
#na tela uma das mensagens abaixo:
#- O primeiro valor é o maior
 #- O segundo valor é o maior
 #- Não existe valor maior, os dois são iguais

A=int(input("Digite um número "))
B=int(input("Digite outro número "))

if(A>B):
     print("O primeiro valor é o maior")
if(B>A):
    print("O segundo valor é o maior")
if(A==B):
    print("Não existe valor maior, os dois são iguais")