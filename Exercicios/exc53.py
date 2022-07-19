# 53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos



contador=1
homens=0
mulheres=0
somagrupo=0
somahomens=0
mMaior20=0
pessoa=3

while(contador<=pessoa):
    idade=int(input(("Idade da "+ str(contador) +"ª pessoa:")))
    Sexo=(input(("Sexo da "+ str(contador) +"ª pessoa:"))).upper()
    

    if(Sexo=="M"):
        homens=homens+1
        somahomens=somahomens+idade 

        
    if(Sexo=="F"):
        mulheres=mulheres+1
    if((Sexo=="F") and (idade>20)):
        mMaior20=mMaior20+1
   
    
    
    somagrupo=somagrupo+idade
    contador=contador+1

Mediahomens=(somahomens/((homens)))
Mediagrupo=(somagrupo/((pessoa)))

    

print("Qtd de homens:" + str(homens)) 
print("Qtd de mulheres: " + str(mulheres))
print("A média da idade do grupo é" + str(Mediagrupo))
print("A média da idade do homens é" + str(Mediahomens))
print("Qtd mulheres maiores de 20 anos: "+ str(mMaior20))

    

    

   
