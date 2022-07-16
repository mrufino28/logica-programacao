#33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra 
#de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e 
#em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que 
#ela não pode exceder 30% do salário ou então o empréstimo será negado.

Vl_casa=float(input("Qual o valor da Casa: "))
S=float(input("Qual o seu salário? "))
Anos=int(input("Quantis meses de pagamento? "))
Prest=Vl_casa/Anos

if(Prest<=S*0.3):
    print("O valor da prestacão será de: " + str(Prest))
else:
    print("Você não pode financiar esse imóvel")