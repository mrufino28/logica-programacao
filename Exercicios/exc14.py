##14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
##um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
##quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
##sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado

KM=float(input("Digite o km pecorrido pelo veiculo:"))
Qtd_dias= int(input("Digite a quantidade de dias de aluguel:"))
P=((90*Qtd_dias)+(0.20*KM))
print("O preço total a pagar é de:R$"+ str(P))