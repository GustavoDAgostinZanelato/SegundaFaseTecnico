""" 21) Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada casoa """

def soma():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = (numero1 + numero2)
    print("A soma dos números digitados é:",operacao)
    print("")
    main()

def multiplicacao():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = (numero1 * numero2)
    print("O produto dos números digitados é:",operacao)
    print("")
    main()

def maior():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    
    if(numero1 > numero2):
        print("O número",numero1,"é maior que o número",numero2)
    else:
        print("O número",numero2,"é maior que o número",numero1)
    print("")
    main()

def menor():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    
    if(numero1 < numero2):
        print("O número",numero1,"é menor que o número",numero2)
    else:
        print("O número",numero2,"é menor que o número",numero1)
    print("")
    main()

def main():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Soma \n2-Multiplicação \n3-Maior que \n4-Menor que \n5-Sair "))

        if(menu == 1):
            soma()
        if(menu == 2):
            multiplicacao()
        if(menu == 3):
            maior()
        if(menu == 4):
            menor()
        if(menu == 5):
            break

main()
