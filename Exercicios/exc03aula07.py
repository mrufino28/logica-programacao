##Cálculo Peso Ideal 

from ast import If


Peso=float(input("Qual seu peso?"))
Altura=float(input("Qual sua altura"))
Imc=(Peso/(Altura**2))
print("Seu IMC é "+ str(Imc))

if((Imc>=18.5) and (Imc<=25)):
    print("Ou seja, você está dentro do peso ideal")
if(Imc<18.5):    
    print("Ou seja, você está abaixo do peso ideal")
else:
    print("Ou seja, você está acima do peso ideal")
