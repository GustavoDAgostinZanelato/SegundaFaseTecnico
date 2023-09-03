""" 5) Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. """

metros = int(input("Insira um valor em metros: "))

cm = (metros * 100)
mm = (metros * 1000)

print(metros,"metro(s) é equivalente a", cm,"centímetros e",mm,"milimetros")