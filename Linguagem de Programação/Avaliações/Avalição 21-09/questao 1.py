def main():
    while True:
        #Informa qual será o calculo
        menu = int(input("Selecione qual Área Calcular: \n 1- Área do Círculo \n 2- Área Triângulo \n 3- Área do Retângulo \n 4- Área do Losângulo \n 5- Sair "))
        
        #Condições para chamar a função dos calculos
        if (menu == 5):
            break
        
        if (menu == 1):
            print(circulo())
        
        elif (menu == 2):
            print(triangulo())
        
        elif (menu == 3):
            print(retangulo())
        
        elif (menu == 4):
            print(losangulo())
        
        #Condição caso nenhum dos números seja descrito
        else:
            print("Erro, Digite uma opção válida")
        

#Calcula e retorna o valor do circulo
def circulo():
    raio = float(input("Insira o Raio do cículo: "))       
    area = 3.14 * (raio * raio)
    return area

#Calcula e retorna o valor do triangulo
def triangulo():
    base = float(input("Insira o valor da Base: "))
    altura = float(input("Insira o valor da Altura:"))
    area = (base * altura) /2
    return area

#Calcula e retorna o valor do retangulo
def retangulo():
    comprimento = float(input("Insira o valor do Comprimento: "))
    largura = float(input("Insira o valor da Largura: "))
    area = comprimento * largura
    return area

#Calcula e retorna o valor do losangulo
def losangulo():
    diagonal_maior = float(input("Insira o valor da diagonal Maior: "))
    diagional_menor = float(input("Insira o valor da diagonal Menor: "))
    area = (diagional_menor * diagonal_maior) /2
    return area


main()