""" 7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% 
de aumento """

preco = float(input("Digite o preço do produto: "))

desconto = (preco * 0.05)
novo_valor = (preco - desconto) 
aumento = (novo_valor * 1.15)

print("O novo preço do produto é de",aumento)
