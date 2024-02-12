""" 14) Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista."""

nomes = ["Gustavo", "João", "Pedro", "Maria"]

print(nomes)
finder = str(input("Digite o nome que você deseja localizar na lista: "))
if (finder in nomes):
    print("Sim,",finder, "está na lista")
else:
    print("Esse item não está na lista")

index = (nomes.index(finder))

print("O nome",finder,"está no index",index)