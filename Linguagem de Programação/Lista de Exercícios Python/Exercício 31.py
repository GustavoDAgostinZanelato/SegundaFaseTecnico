""" 31) Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador 
perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo. """

import random
numero_maquina = random.randint(1, 10)
vitorias_consectivas = []

def jogar():
    lado = int(input("Escolha seu lado: \n1-Ímpar \n2-Par "))
    if(lado == 1):
        print("Você escolheu Ímpar")

    if(lado == 2):
        print("Você escolheu Par")
    
    numero_jogador = int(input("Digite um número entre 1 e 10: "))
    if(numero_jogador > 10) or (numero_jogador < 0):
        print("Número Inválido")
        print("")
        main()
    else:
        soma = (numero_jogador + numero_maquina)
        resultado = (soma % 2)

        if(lado == 1) and (resultado == 1):
            print("Você Venceu")
            print("O resultado da soma foi de:",soma)
            print("")
            vitorias_consectivas.append(1)
            main()

        elif(lado == 2) and (resultado == 0):
            print("Você Venceu")
            print("O resultado da soma foi de:",soma)
            print("")
            vitorias_consectivas.append(1)
            main()
        
        else:
            print("Você Perdeu")
            print("O resultado da soma foi de:",soma)
            print("Você venceu",len(vitorias_consectivas),"vezes consecutivas")
            print("")
            main()

def main():
    while True:
        print("Jogo de Ímpar ou Par")
        menu = int(input("Como deseja proseguir: \n1-Jogar \n2-Sair "))

        if(menu == 1):
            jogar()
        if(menu == 2):
            break
main()
