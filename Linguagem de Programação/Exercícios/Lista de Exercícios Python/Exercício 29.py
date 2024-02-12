""" 29) O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o 
cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o 
cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos 
itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que 
monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
a. Lojas Quase Dois - Tabela de preços
b. 1 - R$ 1.99
c. 2 - R$ 3.98
d. ...
e. 50 - R$ 99.50 """


qtd_produtos = int(input("Quantos produtos o cliente deseja comprar: "))

def tabela():
    indice = 1
    for i in range(50):
        print(f"{i+1}- R$",1.99 * indice)
        indice = indice + 1

def main():
    while True:
        valor = (qtd_produtos * 1.99)
        print("O valor de compra será de",valor,"reais")

        pergunta = str(input("Deseja consultar a tabela de Preços (S/N): "))
        if(pergunta == "N"):
            break
        else:
            tabela()
            break
main()
