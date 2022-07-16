#47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 
#450 + 400 + 350 + 300 + ... + 50 + 0

contador=500
soma=0

while(contador>=0):
    print(contador)
    soma=(soma+contador)
    contador=contador-50

print(soma)