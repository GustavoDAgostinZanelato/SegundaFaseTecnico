""" 9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma 
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para 
Euros."""

nome = str(input("Digite seu nome: "))
reais = float(input("Digite quantos reais você possui: "))

dolar = (reais / 4.87)
euro = (reais / 5.27)

print(nome,", com",reais,"reais você consegue comprar",dolar,"dollars e",euro,"euros")