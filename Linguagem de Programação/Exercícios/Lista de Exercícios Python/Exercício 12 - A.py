""" 12 - A) Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre 
os itens repetidos.  """

lista = ["João", "João", "Pedro", "Marcos", "Marcos"]

verificador1 = (lista.count("João"))
if(verificador1 > 1):
    print("João aparece",verificador1,"vezes na lista")

verificador2 = (lista.count("Pedro"))
if(verificador2 > 1):
    print("Pedro aparece",verificador2,"vezes na lista")

verificador3 = (lista.count("Marcos"))
if(verificador3 > 1):
    print("Marcos aparece",verificador3,"vezes na lista")

