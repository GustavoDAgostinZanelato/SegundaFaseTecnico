""" 30) O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de 
conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá 
receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser 
informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e 
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta 
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser 
conforme o exemplo abaixo:
a. Lojas Tabajara 
b. Produto 1: R$ 2.20
c. Produto 2: R$ 5.80
d. Produto 3: R$ 0
e. Total: R$ 8.00
f. Dinheiro: R$ 20.00
g. Troco: R$ 12.00
h. ... """

produto1 = 2.20
produto2 = 5.80

def main():
    while True:
        resposta = str(input("Deseja efetuar uma venda (S/N)")) #Valor zero substituido por (S/N)
        if(resposta == "N"):
            break
        
        if(resposta == "S"):
            p1 = int(input("Informe a quantidade do produto 1 que o cliente deseja comprar: ")) #Quantidade de 1
            p2 = int(input("Informe a quantidade do produto 2 que o cliente deseja comprar: ")) #Quantidade de 1
            total = (produto1 * p1 + produto2 * p2) #Resultado deve ser 8
            print("O total da compra foi de",total)

            dinheiro = float(input("Qual nota o cliente entregou: ")) #Nota de 20
            troco = (dinheiro - total)

            print("O troco que deverá ser dado ao cliente é de",troco,"reais")
            print("")

main()
