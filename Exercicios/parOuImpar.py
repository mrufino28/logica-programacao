# lê entrada do usuário e atribui a var qtd_vezes
qtd_vezes = int(input("Quantos numeros vc quer testar?"))


#inicia bloco de repetição testando qtd_vezes, se for maior que 0 entra no bloco
while(qtd_vezes > 0):
    #lê entrada do usuário e atribui a var
    numero_Digitado = int(input("Digite o valor: "))
    #calcula o resto da divisão por 2 do valor digitado anteriormente 
    resto_divisao = numero_Digitado % 2
    #testa se o resto é 0, resultando em um valor par
    if(resto_divisao == 0):
        #printa é par
        print("É par!")
    #se não entrar no if, vem para o else    
    else:
        #printa é impar
        print("É impar!")
    #decrementa o contador do while, fazendo com que o mesmo se encerre em algum momento
    qtd_vezes = qtd_vezes - 1