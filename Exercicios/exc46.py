#46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 
#8 + 10 + 12 + 14 + ... + 98 + 100.

contador=6
soma=0

while(contador<=100):
    print(contador)
    soma=contador+soma
    contador=contador+2
    
print(soma)    
   