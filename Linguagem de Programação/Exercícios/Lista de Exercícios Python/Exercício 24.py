""" 24) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido """

while True:
    nota = float(input("Digite uma nota menor que dez e maior que zero: "))

    if(nota >= 10) or (nota <= 0):
        print("Valor Inválido")
        print("")
    
    else:
        print("Nota Digitada:",nota)
        break