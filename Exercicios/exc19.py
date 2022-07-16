##19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua 
##média e mostre na tela. No final, analise a média e mostre se o aluno teve ou 
##não um bom aproveitamento (se ficou acima da média 7.0).

Nota1=float(input("Primeira Nota:"))
Nota2=float(input("Segunda Nota:"))
Media=(Nota1+Nota2)/2
print("Média: " + str(Media))

if(Media>=7):
    print("APROVADO")
else:
        print("REPROVADO")
