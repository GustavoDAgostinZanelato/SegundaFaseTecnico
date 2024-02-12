""" Revisão de Funções """

# funcoes com e sem parametro, return, print  lsita dentro de lista
""" Exemplo 1 """
# def inicio():
#     print("Revisão Função")

# inicio()


""" Exemplo 2 """
# def flores():
#     global flor
#     flor = input("Digite uma flor: ")
#     cor = input("Digie a cor da flor: ")
#     print("A flor digitada foi",flor,"e a sua cor é",cor)

# flores()
# print(flor)


""" Exemplo 3 """
# def name(n):
#     print("-" * 30)
#     print("Olá",n,"seja bem vindo")
#     print("-" * 30)

# name("Gustavo")
# name("Pedro")
# name("João")
# name()


""" Exemplo 4 """
# def somar(a,b,s):
#     s = a + b + s
#     print(f"A soma do valor",a,"e do valor",b,"resulta em",s)

# somar(1,3,6)
# somar()


""" Exemplo 5 """
# def somar(*n):
#     soma = sum(n)
#     tamanho = len(n)
#     print("A soma dos valores é",soma,"e a quantidade de itens é",tamanho)

# somar(2,3,4,5,6)
# somar(2,3)


""" Exemplo 6 """
# def somar(a,b):

#     s = a + b
#     return s

# n = int(input("n: "))
# c = int(input("c: "))
# a = somar(4,5)
# print(a)


""" Exemplo 7 """
# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# print(par(3))
# print(par(2))


""" exemplo 8 """
# def cadastro():
#     nome = input("Digite o seu nome: ")
#     idade = input("Digite a sua idade: ")
#     return nome, idade

# print("Iniciando cadastro...")
# name, age = cadastro()
# print("Cadastro Realizado")
# print("Seu nome é",name,"e sua idade é",age)


""" exemplo 9 """

def soma():
    conta = valor + valor2
    return conta


def subtacao():
    conta = valor1 - valor2
    return conta


def multiplicacao():
    conta = valor1 * valor2
    return conta
    

def divisao():
    conta = valor1 / valor2
    return conta


def main():
    while True:
        menu = int(input("Digite como prosseguir: \n1-Soma \n2-Subtação \n3-Multiplicação \n4-Divisão \n5-Sair "))

        if(menu == 5):
            break

        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))

        if(menu == 1):
            print(soma(a,b))

        elif(menu == 2):
            print(subtacao(a,b))

        elif(menu == 3):
            print(multiplicacao(a,b))

        elif(menu == 4):
            print(divisao(a,b))
        else:
            print("Selecione uma opçâo válida")
     
main()


