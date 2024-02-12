""" 27) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 """

numero = int(input("Digite um número inteiro: "))

def fatorial(numero):
    if (numero == 0) or (numero == 1):
        return 1
    else:
        return numero * fatorial(numero - 1)

resultado = fatorial(numero)
print("O rasultado do fatorial do número",numero,"é:",resultado)
