#42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo 
#qualquer e mostre uma contagem até esse valor:
#Ex: Digite um valor: 35
#Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

CONTADOR=0
N=int(input("Até quanto você quer contar:"))


while(CONTADOR<=N):
    print(CONTADOR)
    CONTADOR=CONTADOR+1
print("Acabou")
