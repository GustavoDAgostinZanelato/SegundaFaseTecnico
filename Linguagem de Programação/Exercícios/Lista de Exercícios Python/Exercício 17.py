""" 17) Faca um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
utilizando as seguintes formulas (onde h corresponde à altura): 
• Homens: (72.7 * h) - 58 
• Mulheres: (62, 1 *  h) - 44, 7 """


nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
sexo = str(input("Qual o seu sexo Masculino(M) ou Feminino(F): "))

if(sexo == "M"):
    peso_idealM = (72.7 * altura) - 58
    print(nome,", seu peso ideal baseado na sua altura é de:",peso_idealM)

if(sexo == "F"):
    peso_idealF = (62.1 * altura) - 44.7
    print(nome,", seu peso ideal baseado na sua altura é de:",peso_idealF)
