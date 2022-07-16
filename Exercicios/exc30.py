#30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
#de triângulo será formado: 
 #- EQUILÁTERO: todos os lados iguais
 #- ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

A=int(input("Qual o valor de A:"))
B=int(input("Qual o valor de B:"))
C=int(input("Qual o valor de C:"))

if((A+B>C) and (A+C>B) and (C+B>A) ):
    print("Pode formar um triângulo") 
    if(A==B==C):
        print("Triângulo Equilátero")
    if((A==B!=C) or (C==A!=B) ):
        print("Triângulo Isósceles")
    if(A!=B!=C and A!=C):
        print("Triângulo Escaleno")

else:
    print("Não Pode formar um triângulo")