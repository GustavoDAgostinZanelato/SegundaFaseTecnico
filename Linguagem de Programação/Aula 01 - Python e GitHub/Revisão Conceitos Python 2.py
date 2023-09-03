lista = ["Matheus", "Marcelo", "Andrey", "Pedro", "Davi", "Davi", "Davi"]
#            0          1          2        3
#           -4         -3         -2       -1

""" Exibindo a Lista """
# print(lista[2]) 
# print(-4)
# print(lista[4]) Error!


""" #Adicionando Itens na Lista """
#lista.append("Gustavo")
# print(lista)


""" Adicionando em uma Posição Declarada """
lista.insert(0, "João")
# print(lista)
#lista[0]="André"
# print(lista)


""" Exibindo Itens a Partir de um Intervalo de Index """
# print(lista[:3]) #Antes do Index 3
# print(lista[3:]) #Depois dd Index 3
# print(lista[1:4]) #Entre 1 a 3 index


""" Deletando Itens de Lista Pelo Index """
# print(lista) 
# del lista[0] #Deleta o item do index menciondo
# print(lista)
# del lista[4] #Deleta o item do index menciondo
# print(lista)
# del lista[0:3] #Deleta Entre o intervalo dos Index de 0 a 2
# print(lista)


""" Deletando Itens de Lista Pelo Nome """
# lista.remove("Davi") #Caso a lista apresente mais de um Davi, o "remove" vai deletar somente a 1º aparição do nome
# print(lista)


""" Deletando Itens de Lista Pelo Index porém Salvando em outra Variável """
# lista.pop(0)
# print(lista)

# b = lista.pop(0)
# print(b)
# print(lista)


""" Limpando a lista """
# lista.clear() #Limpa mas não deleta a lista
# print(lista)


""" Copiando uma Lista """
lista2 = lista.copy()
# print(lista)
# print(lista2)


""" Juntando/Concatenando Listas """
lista3 = lista + lista2
# print(lista)
# print(lista3)


""" Contando os Itens de uma Lista """
# print(lista3.count("João")) #Conta quantos itens possuem o nome "João"
# print(len(lista3)) #Conta quantos itens tem na lista


""" Verifica em qual Index algum Item se encontra na Lista """
# print(lista.index("Pedro"))


""" Ordenação de Lista """
val = [22,45,12,0,4,2,1,6,144,43]
# val.sort() #Coloca em ordem CRESCENTE - Funciona também em ordem alfabética
# print(val)

# val.reverse() #Coloca em ordem DECESCENTE - Funciona também em ordem alfabética
# print(val)


""" Valor Mínimo, Máximo e Soma """
# min = min(val)
# max = max(val)
# soma = sum(val)
# print("Valor Mínimo:", min, "\nValor Máximo: ",max, "\nSoma: ",soma)


""" Verificando se um Item está na Lista """
# print(lista)
# if "Pedro" in lista:
#     print("Sim, Pedro está na lista")
# else:
#     print("Esse item não está na lista")

# del lista[4]
# print(lista)

# if "Pedro" in lista:
#     print("Sim, Pedro está na lista")
# else:
#     print("Esse item não está na lista")


""" Uso do For"""
# for i in lista:
#     if "Davi" in lista:
#         lista.remove("Davi")
#     print(i)
# print(lista)


""" Uso do While """
while True:
    professor = input("Digite um professor do Curso: ")
    if professor == "mari":
        print("Correto")
        break
    