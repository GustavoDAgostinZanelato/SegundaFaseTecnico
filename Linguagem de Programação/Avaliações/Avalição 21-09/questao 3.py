nome = []
preco = []
quantidade = []
valor_compra = []
lista_geral = []
# def com um breve menu para o programa
def main():
    while True:
        print("Boas vindas a Loja ABC")
        menu = int(input("Como desejas continuar? \n1-Inserir Mercadoria \n2-Sair \n"))
        
        if (menu == 2):
            break
        if (menu == 1):
            inserir()
        else:
            print("Digite uma opção válida")
    

# def que recebe as informações do nome, valor e quantidade de produtos 
def inserir():
    while True:
        produto = str(input("Insira o nome do produto: ")) 
        nome.append(produto)
        valor = float(input("Insira o valor do produto: "))
        preco.append(valor)
        qtd = int(input("insira a quantidade que deseja comprar: "))
        quantidade.append(qtd)
        lista_secundaria = ['Produto:', produto, 'Valor:', valor, 'Quantidade:', qtd] 
        lista_geral.append(lista_secundaria)
        
        sair = str(input("Digite 'fim' para sair ou precione enter para continuar: \n "))
        if (sair == "fim"):
            break
    calcular_total(preco, quantidade)

         
# def que calcula o preco final da compra
def calcular_total(preco, quantidade):
    soma1 = sum(preco)
    soma2 = sum(quantidade)
    total = soma1 * soma2
    valor_compra.append(total)
    imprimir_recibo(nome, quantidade, preco, valor_compra)
    

# def que mostra o recibo da compra ao cliente
def imprimir_recibo(nome, quantidade, preco, valor_compra):
    print(lista_geral)
    print("O valor total da compra foi de: ",valor_compra,"\n")
    
main()