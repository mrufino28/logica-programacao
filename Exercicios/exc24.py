##24) Faça um algoritmo que pergunte a distância que um passageiro deseja 
##percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
##viagens até 200Km e R$0.45 para viagens mais longas.

Km=float(input("Qual distância a ser pecorrida:"))
if(Km<=200):
    preço=0.50*Km
    print("O preço da passagem é "+ str(preço))
else:
    preço=0.45*Km
    print("O preço da passagem é "+ str(preço))