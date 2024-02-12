""" 22) Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for 
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles. 
Desconsiderando o valor 1000 da parada. """

numeros = []

while True:
    valores = int(input("Digite um valor inteiro positivo diferente de mil: "))

    if(valores != 1000):
        numeros.append(valores)

    else:
        break

soma = sum(numeros)
print(numeros)
print("O total de números digitados foi de:",len(numeros))
print("A soma de todos os números digitados é de:",soma)
        
