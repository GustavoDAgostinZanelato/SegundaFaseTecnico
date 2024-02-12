# CRUD = Create, Read, Update, Delete - Nome dado a comunicação Python/SQL

import mysql.connector #Realiza a conexão entre Python e SQL

#Criando a conexão com o banco
conexao = mysql.connector.connect(
    host='127.0.0.1', #Valor do IP host presente no próprio banco de dados
    user='root', #Rede que estamos conectados
    password='', #A rede nao possui senha
    database='merceariajeremias', #nome do banco que desejo acessar
)
cursor = conexao.cursor()


#-----------------------------------------------------------------------------------------------------------------------#


""" #Linhas de código para inserir informações/valores na tabela do MySQL"""
# nome_do_produto = "abacaxi"
# valor_do_produto = 3.50
# comando = f'INSERT INTO vendas (nome_produto, vendascol) VALUES ("{nome_do_produto}", "{valor_do_produto}")' 
# #O comando SQL nescessita estar entre aspas simples. Variáveis String nescessitam estar entre aspas duplas
# cursor.execute(comando) #executa o variável "comando"
# conexao.commit() #Manda e modifica as informaçoes do BD

# nome_do_produto = "melão"
# valor_do_produto = 11.50
# comando = f'INSERT INTO vendas (nome_produto, vendascol) VALUES ("{nome_do_produto}", {valor_do_produto})' 
# cursor.execute(comando)
# conexao.commit()



""" Selecionando Informações na Tabela """
# comando = f'SELECT * FROM vendas' #Selecionada tudo da tabela "vendas"
# cursor.execute(comando)
# resultado = cursor.fetchall() #Lê o banco de dados


""" Selecionando Informações na Tabela 2 """
#                     0                1  
# resultado = [(0,abacaxi,3.50),(1,melão,11,50)]  ----> Esse é o modo que a table do SQL é interpretada pelo Python
#               0     1     2    0    1     2

# print(resultado) #Mostra no monitor serial o resultado da pesquisa em forma de tupla (uma lista imutável)
# print(resultado[0]) #Mostra somente a linha do abacaxi
# print(resultado[1]) #Mostra somente a linha do melão
# print(resultado[1][1]) #Mostra o nome "Melão" 
# print(resultado[1][0]) #Mostra o código referente ao melão



""" Selecionando Informações na Tabela 3 """
# #                0                  1
# lista = [(5,"Abacaxi",3.5) , (6,"Melão",4.8)]
# #          0     1     2      0     1     2     

# for i in lista:
#     print(i[1]) # Mostra "Abacaxi" na primeira vez que rodar, e "Melão" na segunda
#     print(i[0]) # Mostra os  valores 5 e 6
#     print(i[2]) # Mostra os valores 3.5 e 4.8



""" Percorrendo toda a lista """

""" Primeiro Método """
# print("ID, Produto, Preço") #Mostra inicialemente as colunas da tabela
# for i in range(len(resultado)): #A variável "i" será de acordo com o tamanho da lista "resultado"
#     print(resultado[i][0],resultado[i][1],resultado[i][2]) #A variável "i" representa o número de linhas da tabela

""" Segundo Método """
# print("ID, Produto, Preço") #Mostra inicialemente as colunas da tabela
# for i in resultado: #Ao invés de percorrer cada item da lista, "i" irá percorrer somente a lista
#     print(i) #Exibindo o valor da variável



""" Deletando itens da lista """
# nome_produto = "melão"  # será deletado somento o nome "melão"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()



""" Atualizando itens na Tabela """
# comando = f'UPDATE vendas SET nome_produto = "{"Morango"}"' # O produto "Abacaxi agora é "Morango"
# comando = f'UPDATE vendas SET vendascol = "{10.0}" WHERE nome_produto = "Morango"' # Troca o preço do morango para 10
# cursor.execute(comando)
# conexao.commit()



""" Criando uma nova Tabela """
# comando = f'CREATE TABLE Atendentes (codigo int(5), nome varchar(10))' #Variável que apresenta o comando SQL
# cursor.execute(comando)
# conexao.commit() 





""" Atualizando Nome e Valor dos Produtos com um Menu """

# def nome():
#     print("")
#     print("ID, Produto, Preço")
#     for i in resultado: 
#         print(f'{i[0]} {i[1]} {i[2]}')

#     index = int(input("Digite o ID correspondente: "))
#     novo_nome = str(input("Digite o novo nome do produto: "))

#     if (index > len(resultado)):
#         print("ERRO. Digite um index válido")
#         print("")
#         main()

#     comando = f'UPDATE vendas SET nome_produto = "{novo_nome}" WHERE idvendas = "{index}" '
#     cursor.execute(comando)
#     conexao.commit()


# def valor():
#     print("")
#     print("ID, Produto, Preço")
#     for i in resultado: 
#         print(f'{i[0]} {i[1]} {i[2]}')

#     index = int(input("Digite o ID correspondente: "))
#     novo_valor = float(input("Digite o novo valor do produto: "))

#     if (index > len(resultado)):
#         print("ERRO. Digite um index válido")
#         print("")
#         main()

#     comando = f'UPDATE vendas SET vendascol = "{novo_valor}" WHERE idvendas = "{index}" '
#     cursor.execute(comando)
#     conexao.commit()


# def main():
#     while True:
#         print("Lista dos Produtos")
#         print("ID, Produto, Preço")
#         for i in resultado: 
#             print(f'{i[0]} {i[1]} {i[2]}')
#         print("")

#         menu = int(input("Como deseja proseguir: \n1-Modificiar NOME do produto \n2-Modificar VALOR do produto \n3-Sair  "))

#         if(menu == 3):
#             break

#         if(menu == 1):
#             nome()
        
#         elif(menu == 2):
#             valor()

# main()





""" Criar, Modificar, Deletar e Exibir itens com estrutura de Menu """

# def criar():
#     print("Lista dos Produtos")
#     print("ID, Produto, Preço")
#     for i in resultado: 
#         print(f'{i[0]} {i[1]} {i[2]}')
    

# def modificar():
#     print("Lista dos Produtos")
#     print("ID, Produto, Preço")
#     for i in resultado: 
#         print(f'{i[0]} {i[1]} {i[2]}')


# def main():
#     while True:
#         print("Lista dos Produtos")
#         print("ID, Produto, Preço")
#         for i in resultado: 
#             print(f'{i[0]} {i[1]} {i[2]}')
#         print("")

#         menu = int(input("Como deseja proseguir: \n1-Criar coluna \n2-Modificar Tabela \n3-Deletar itens \n4-Exibir \n5-Sair"))

#         if(menu == 5):
#             break

#         if(menu == 1):
#             criar()

#         # elif(menu == 2):
#         #     modificar()

#         # elif(menu == 3):
#         #     deletar()
        
#         # elif(meu == 4):
#         #     exibir()
    
# main()