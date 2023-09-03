""" 16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit 
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida 
conversão. """

while True:
    temp = float(input("Digite qual é a temperatura atual: "))
    resposta = str(input("Você deseja saber essa temperatura em Fahrennheit (S/N)? "))

    if(resposta == "N"):
        break
    if(resposta == "S"):
        calculo = (temp * 9/5) + 32
        print(temp,"graus célcius quivalem a",calculo,"graus Fahrennheit")
        break