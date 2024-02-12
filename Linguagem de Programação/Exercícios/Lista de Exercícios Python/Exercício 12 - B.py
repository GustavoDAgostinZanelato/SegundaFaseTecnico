""" 12 - B) Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte. """

filmes = []
jogos = []
livros = []
esportes = []

print("Insira dois itens na lista Filmes: ")
for i in range(2):
    movie = str(input("Filmes: "))
    filmes.append(movie)
print(filmes)


print("Insira dois itens na lista Jogos: ")
for i in range(2):
    game = str(input("Jogos: "))
    jogos.append(game)
print(jogos)


print("Insira dois itens na lista Livros: ")
for i in range(2):
    book = str(input("Livros: "))
    livros.append(book)
print(livros)


print("Insira dois itens na lista Esportes: ")
for i in range(2):
    sport = str(input("Esportes: "))
    esportes.append(sport)
print(esportes)


nova_lista = (filmes + jogos + livros + esportes)
print(nova_lista)


index = int(input("Digite o index do item da lista livros que você deseja exibir (sua lista possui 2 itens): "))
print(livros[index]) 


index2 = int(input("Digite o index do item da lista esporte que você deseja excluir (sua lista possui 2 itens): "))
del esportes[index2]
print(esportes)
