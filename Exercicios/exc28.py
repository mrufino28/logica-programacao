#28) Faça um programa que leia a largura e o comprimento de um terreno 
#retangular, calculando e mostrando a sua área em m². O programa também 
#devemostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m² = TERRENO POPULAR
 #- Entre 100m² e 500m² = TERRENO MASTER
#- Acima de 500m² = TERRENO VIP

L=int(input("Digite a largura: "))
A=int(input("Digite a altura: "))
Area=L*A
print("A área do terreno é de "+ str(Area))
if(Area<100):
    print("TERRENO POPULAR")
if(100<Area<=500):
    print("TERRENO MASTER")
        
if(Area>500):
    print("TERRENO VIP")
