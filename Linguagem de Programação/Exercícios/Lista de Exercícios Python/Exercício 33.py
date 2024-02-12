""" 33) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os 
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o 
valor zero """

matheus = []
gabriel = []
pedro = []
maria = []
branco = []
contador = 0


def candidato1 ():

    voto1 = str(input("Comfirmar voto em candidato Matheus (S/N): "))

    if(voto1 == "S"):
        print("Voto Confirmado")
        matheus.append(voto1)
    else:
        main()


def candidato2 ():

    voto1 = str(input("Comfirmar voto em candidato Gabriel (S/N): "))

    if(voto1 == "S"):
        print("Voto Confirmado")
        gabriel.append(voto1)
    else:
        main()


def candidato3 ():

    voto1 = str(input("Comfirmar voto em candidato Pedro (S/N): "))

    if(voto1 == "S"):
        print("Voto Confirmado")
        pedro.append(voto1)
    else:
        main()


def candidato4 ():

    voto1 = str(input("Comfirmar voto em candidato Maria (S/N): "))

    if(voto1 == "S"):
        print("Voto Confirmado")
        maria.append(voto1)
    else:
        main()


def voto_branco ():

    branco_voto = str(input("Confirmar voto em branco (S/N): "))

    if (branco_voto == "S"):
        print("Voto Confirmado")
        branco.append(branco_voto)
    else:
        main()


def voto_nulo ():

    branco_nulo = str(input("Confirmar voto nulo (S/N): "))

    if (branco_nulo== "S"):
        print("Voto Confirmado")
        branco.append(branco_voto)

    else:
        main()


def mais_votado ():

    if(len(machado) > len(alencar)) :
        print("O candidato mais votado foi MACHADO DE ASSIS,com: ",len(machado),"votos")
        print("votos em branco:",len(branco))
        print("José de Alencar recebeu: ", len(alencar), "votos")

    elif(len(alencar) > len(machado)):
        print("O candidato mais votado foi JOSÉ DE ALENCAR,com:",len(alencar),"votos")
        print("A quantidade de votos em branco foi de:", len(branco))
        print("Machado de Assis recebeu: ",len(machado),"votos")


def main():
    while True:

        menu = int(input("Como deseja proseguir: \n1-Candidato Matheus \n2-Candidato Gabriel \n3-Candidato Pedro \n4-Candidato Maria \n5-Voto em Branco \n6-Voto Nulo \n7-Resultado \n8 -Sair  "))

        if (menu == 1):
            candidato1()
        if (menu == 2):
            candidato2()
        if (menu == 3):
            candidato3()
        if (menu == 4):
            candidato4()

        if (menu == 5):
            voto_branco()
        if (menu == 6):
            voto_nulo()

        if (menu == 7):
            mais_votado()
        if (menu == 8):
            break

main()
