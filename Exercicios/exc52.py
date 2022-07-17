# 52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

from statistics import mean


contador=1
mais18=0
menos5=0
maior=0
soma=0

while(contador<=5):
    idade=int(input("Qual sua idade: "))
    soma=soma+idade
   
    if(idade>18):
        mais18=mais18+1
    if(idade<5):
        menos5=menos5+1
    if(idade>maior):
        maior=idade
    
    contador=contador+1

print(mais18)
print(menos5)
print(maior)
print(soma/(contador-1))
