##
#22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
#situação em relação ao alistamento militar.
 #- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
#alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
#alistamento.

Ano_nasc=int(input("Qual o ano do seu nascimento?"))
Idade=2022-Ano_nasc
print(Idade)
if(Idade<18):
    F=(18-Idade)
    print("Faltam " + str(F)+ " anos para o alistamento")
else:
    P=(Idade-18)
    print("Passaram " + str(P)+ " anos do alistamento")