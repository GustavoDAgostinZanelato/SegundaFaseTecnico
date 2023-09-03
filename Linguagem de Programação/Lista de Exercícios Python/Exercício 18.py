""" 18) Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem 
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi 
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos."""

prova1 = float(input("Digite a nota da primeira prova peso 5: "))
prova2 = float(input("Digite a nota da segunda prova peso 5: "))
prova3 = float(input("Digite a nota da prova de peso 10: "))

soma = (prova1 + prova2)

media = (soma + prova3)/2

if(media >=7 ):
    print(media)
    print("Aluno Aprovado")

if(media < 7):
    print(media)
    print("Aluno Reprovado")