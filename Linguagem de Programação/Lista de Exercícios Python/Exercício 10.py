""" 10) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58 """

nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))

calculo = ((72.7*altura) - 58)

print(nome,"seu peso ideal beseado na sua altura de",altura,"é de:",calculo)