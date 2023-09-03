""" Exercício 7 """

produtos = []

def compra():
        print("Insira os valores dos produtos")
        x = int(input("Quantos produtos o cliente comprou: "))

        for i in range (x):
            prod = float(input("Valor do Produto: "))
            produtos.append(prod)

        total = sum(produtos)
        print("Total: R$",total)

        pergunta = float(input("Insira oa valor dado pelo cliente para saber o troco: "))
        print("Dinheiro:",pergunta)
        troco = (pergunta - total)
        print("troco:",troco)
        main()

def main():
    while True:
        menu = int(input("Deseja realizar uma venda: \n1-Sim \n2-Sair "))
        
        if(menu == 1):
            compra()

        if(menu == 2):
            break
main()

