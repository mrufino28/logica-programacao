##25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. 
##Analise seus comprimentos e diga se é possível formar um triângulo com essas 
##retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento 
##de cada lado deve ser menor que a soma dos outros dois

A=int(input("Qual o valor de A:"))
B=int(input("Qual o valor de B:"))
C=int(input("Qual o valor de C:"))

if((A+B>C) and (A+C>B) and (C+B>A) ):
    print("Pode formar um triângulo")
else:
    print("Não Pode formar um triângulo")