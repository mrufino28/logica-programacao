## Desenvolva uma lógica que leia os valores de A, B e C de uma equação do 
##segundo grau e mostre o valor de Delta

A= float(input("Digite o valor de a:"))
B= float(input("Digite o valor de b:"))
C= float(input("Digite o valor de c:"))
Delta=((B**2)-(4*A*C))
print("O Valor de DElta é:" + str(Delta))