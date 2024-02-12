""" 19) Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida. 
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção: 
a. Soma de 2 números. 
b. Diferença entre 2 números (maior pelo menor). 
c. Produto entre 2 números. 
d. Divisão entre 2 números (o denominador não pode ser zero) """

def soma():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = (numero1 + numero2)
    print("A soma dos números digitados é:",operacao)
    main()


def diferenca():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = (numero1 - numero2)
    print("A subtração dos números digitados é:",operacao)
    main()
    

def produto():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = (numero1 * numero2)
    print("O produto dos números digitados é:",operacao)
    main()


def divisao():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    if(numero2 == 0 ):
        print("O denominador não pode ser zero")
        divisao()
    else:
        operacao = (numero1 / numero2)
        print("A divisão dos números digitados é:",operacao)
        main()


def main():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Soma \n2-Diferença \n3-Produto \n4-Divisão \n5-Sair "))

        if(menu == 1):
            soma()
        if(menu == 2):
            diferenca()
        if(menu == 3):
            produto()
        if(menu == 4):
            divisao()
        if(menu == 5):
            break

main()

