#32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o 
#jogador vai tentar descobrir qual foi o valor sorteado.

from asyncio.windows_events import NULL
import random

x = random.randint(1,5)
vl=NULL

while(x!=vl):
    vl=int(input("Digite um número:"))
    if(x==vl):
        print("Você descobriu o valor, parabéns")
    else:
        print("Você errou, tente novamente!")
