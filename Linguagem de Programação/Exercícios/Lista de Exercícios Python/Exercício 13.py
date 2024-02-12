""" 13) Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles. """

lista = []

print("Adicione 5 números na lista: ")
for i in range(5):
    numeros = int(input("Número: "))
    lista.append(numeros)

print(lista)

soma = sum(lista)

print("A soma dos intens de lista dos números é de:",soma)