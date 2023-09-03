""" 3) Faça um script que leia duas notas de um aluno e mostre como resultado sua média."""

nome = str(input("Digite o nome do aluno: "))
nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))

media = ((nota1 + nota2)/ 2)

print("A média de notas do aluno", nome, "é de ", media)