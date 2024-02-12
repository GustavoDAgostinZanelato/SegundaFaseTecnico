# def soma(valor1, valor2):
#     conta = (valor1 + valor2)
#     return conta


# def sub(valor1, valor2):
#     conta = (valor1 - valor2)
#     return conta


# def multi(valor1, valor2):
#     conta = (valor1 * valor2)
#     return conta


# def div(valor1, valor2):
#     conta = (valor1 // valor2)
#     return conta


# def menu():
#     while True:
#         menu = int(input("Como deseja prosseguir: \n1-Soma \n2-Subtração \n3-Multiplicação \n4-Divisão \n5-Sair "))

#         if(menu == 5):
#             break
        
#         valor1 = int(input("Digite o primeiro valor: "))
#         valor2 = int(input("Digite o segundo valor: "))

#         if(menu == 1):
#             print(soma(valor1, valor2))

#         elif(menu == 2):
#             print(sub(valor1, valor2))
        
#         elif(menu == 3):
#             print(multi(valor1, valor2))    
        
#         elif(menu == 4):
#             print(div(valor1, valor2))
        
#         else:
#             print("ERRO. Digite uma opção válida")

# menu()

        
# ---------------------------------------------------------------------


# def main(*tupla):
#     tamanho = len(tupla)
#     soma = sum(tupla)
#     maximo = max(tupla)
#     minimo = min(tupla)
#     print("tamanho:",tamanho, "\nsoma:",soma,"\nmaximo:",maximo,"\nminimo:",minimo)
    
# main(1,2,3,4,5)




# def par(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# print(par(3))
# print(par(2))


# def cadastro():
#     nome = input("Digite o seu nome: ")
#     idade = input("Digite sua idade: ")
#     return nome, idade

# name, age = cadastro()
# print(name, age)


# # Criando uma lista de listas
# lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Acessando e editando um elemento da lista interna
# lista_de_listas[0][1] = 99

# # Exibindo a lista após a edição
# print(lista_de_listas)



lista_principal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lista_principal[0][1] = 99
lista_principal[2][2] = 16
lista_principal[1][0] = 256
print(lista_principal)
