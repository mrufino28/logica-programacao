## Desenvolva um programa que leia uma distância em metros e mostre os valores 
##relativos em outras medidas.
N1=int(input("Digite uma medida em metros: "))
km=N1/1000
hm=N1/100
dam=N1/10
print("A distância de "+ str(N1) +" corresponde a:"+ str(km)+"km")
print("A distância de "+ str(N1) +" corresponde a:"+ str(hm)+"hm")
print("A distância de "+ str(N1) +" corresponde a:"+ str(dam)+"dam")
