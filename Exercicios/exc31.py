#Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

# J1=int(input("Escolha um elemento: 1=Pedra, 2=Papel, 3=Tesoura: "))
# J2=int(input("Escolha um elemento: 1=Pedra, 2=Papel, 3=Tesoura: "))
J1=(input("Escolha um elemento: Pedra ,Papel ou Tesoura: ")).upper()
J2=(input("Escolha um elemento: Pedra, Papel ou Tesoura: ")).upper()



if(J1=='PEDRA' and J2=='PEDRA'):
    print("Ninguém ganhou, escolham novamente")
if(J1=='PEDRA' and J2=='PAPEL'):
    print("Papel cobre Pedra: Jogador2 ganhou")
if(J1=='PEDRA' and J2=='TESOURA'):
    print("Pedra quebra tesoura: Jogador1 ganhou")
#
if(J1=='PAPEL' and J2=='PEDRA'):
    print("Papel cobre pedra: Jogador1 ganhou")
if(J1=='PAPEL' and J2=='PAPEL'):
    print("Ninguém ganhou, escolham novamente")
if(J1=='PAPEL' and J2=='TESOURA'):
    print("Tesoura corta papel: Jogador2 ganhou")
#    
if(J1=='TESOURA' and J2=='PEDRA'):
    print("Pedra quebra tesoura: Jogador2 ganhou")
if(J1=='TESOURA' and J2=='PAPEL'):
    print("Tesoura corta papel: Jogador1 ganhou")
if(J1=='TESOURA' and J2=='TESOURA'):
    print("Ninguém ganhou, escolham novamente")
#default
if(J1!='PEDRA' and J1!='TESOURA' and J1!='PAPEL' or J2!='PEDRA' and J2!='PAPEL' and J2!='TESOURA'):
    print('vc digitou errado, animal!')





