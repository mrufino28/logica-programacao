#34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no 
#peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o 
#indivíduo dentro de certas faixas.
# - abaixo de 18.5: Abaixo do peso
#- entre 18.5 e 25: Peso ideal
#- entre 25 e 30: Sobrepeso
#- entre 30 e 40: Obesidade
#- acima de 40: Obseidade mórbida
#Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado 
#da altura)

P=float(input ("Qual o seu peso: "))
A=float(input("Qual sua altura: "))
IMC=(P/A**2)

if(IMC<18.5):
    print("Seu IMC é de "+ str(IMC)+":Você está baixo do peso")
if(18.5<=IMC<25):
    print("Seu IMC é de "+ str(IMC)+":Você está no seu peso ideal")
if(25<=IMC<=30):
    print("Seu IMC é de "+ str(IMC)+":Você está com Sobrepeso")
if(30<=IMC<=40):
    print("Seu IMC é de"+ str(IMC)+":Você está com Obesidade")
if(IMC>40):
    print("Seu IMC é de"+ str(IMC)+":Você está com Obesidade Morbida")