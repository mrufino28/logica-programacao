#44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o 
# #incremento, mostrando em seguida todos os valores no intervalo:
#Ex: Digite o primeiro Valor: 3
#Digite o último Valor: 10
#Digite o incremento: 2
#Contagem: 3 5 7 9 Acabou

#45) O programa acima vai ter um problema quando digitarmos o primeiro valor 
##maior que o último. Resolva esse problema com um código que funcione em qualquer 
#situação


N1=int(input("Digite o último valor: ")) 
N2=int(input("Digite o primero valor: ")) 
IN=int(input("Digite o incremento: "))

if(N1>N2):
    CONTADOR=N2
    while(CONTADOR<=N1):
        print(CONTADOR)
        CONTADOR=CONTADOR+IN
else:
    CONTADOR=N1
    while(CONTADOR<=N2):
        print(CONTADOR)
        CONTADOR=CONTADOR+IN

