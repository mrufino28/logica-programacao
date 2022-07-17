# 51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela 
# qual foi o maior e qual foi o menor preço digitados.

contador=1

while(contador<=8):
    Vl=int(input("Qual o valor do " + str(contador)+"º produto: "))
    if(contador==1 or Vl>maior):
        maior=Vl
    if(contador==1 or Vl<menor):
        menor=Vl
    
    contador=contador+1

print("O maior valor eh: "+str(maior))
print("O menor valor eh: "+str(menor))
