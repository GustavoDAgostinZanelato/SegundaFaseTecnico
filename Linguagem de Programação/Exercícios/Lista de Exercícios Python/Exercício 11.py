""" 11) Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas 
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E 
ao final mostrar seu nome e salário final calculado."""

nome = str(input("Digite o seu nome: "))
num_horas = int(input("Digite seu número de horas trabalhadas na semana: "))
valor_hora = int(input("Digite o valor da hora trabalhada: "))

salario_bruto = (num_horas * valor_hora)
print(nome,",seu salário bruto é de: ",salario_bruto,"reais")

desconto = (salario_bruto * 0.02)
novo_salario = (salario_bruto - desconto)

print(nome,", seu novo salário é de: ", novo_salario,"reais")