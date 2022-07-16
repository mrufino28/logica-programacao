# 50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e 
# mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3

import random

contador=1
Acimade5=0
acima5=[]
Divisivelpor3=0
divivel3=[]
sorteados=[]

while(contador<=20):
    x = random.randint(0,10)
    sorteados.append(x)
    
    if(x>5):
        Acimade5=Acimade5+1
        acima5.append(x)
    if(x%3==0):
        Divisivelpor3=Divisivelpor3+1
        divivel3.append(x)
    contador=contador+1

print (sorteados)
print(str(Acimade5)+" números são acima de 5"+ str(acima5))
print(str(Divisivelpor3)+ " números são divisiveis por 3"+ str(divivel3))
