#49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles 
#são pares e quantos são ímpares.

contador=1
par=0
impar=0

while(contador<=6):
    N=int(input("Digite um número: "))
    if(N%2==0):
        par=par+1
    else:
        impar=impar+1
    contador=contador+1

print(impar)
print(par)