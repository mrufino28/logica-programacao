#48) Faça um programa que leia 7 números inteiros e no final mostre o somatório 
#entre eles.

contador=1
soma=0

while(contador<=7):
    N=int(input("Digite um número:"))
    contador=contador+1
    soma=soma+N
    
print(soma)    