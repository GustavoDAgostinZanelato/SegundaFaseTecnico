""" 15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na 
tela dizendo se está “quente”, “frio” ou “agradável” """

temp = float(input("Digite qual é a temperatura atual em graus célcius: "))

if (temp < 15):
    print("A temperatura está fria")

if ((temp >= 15) & (temp <= 25)):
    print("A temperatura está agradável")

if(temp > 25):
    print("A temperatura está quente")