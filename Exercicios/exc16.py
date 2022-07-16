##16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um 
##fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele 
##já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule 
##quantos dias de vida um fumante perderá e exiba o total em dias


# em 2 anos ele fumou: 7300 cigarros

# perde de vida: 73000 min

# perda de vida em dias: 73000/1440



qtd_cigarros=int(input("Quantos cigarros você fuma por dia?"))
qtd_anos= int(input("Há Quantos anos você fuma?"))
qtd_cigarros_total= qtd_cigarros*qtd_anos*365
min_perdido_vida= qtd_cigarros_total*10
dias_perdidos=min_perdido_vida/1440

print("Dias perdidos de vida é:"+str(dias_perdidos)+ " dias")