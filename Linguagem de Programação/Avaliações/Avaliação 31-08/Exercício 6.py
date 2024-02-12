""" Exercício 6 """

lista = []

while True:
    print("Cadastro da Empresa")

    nome = str(input("Digite o seu nome: "))
    tamanho_nome = len(nome)
    if(tamanho_nome <= 3):
        print("NOME INVÁLIDO")
        break
    else:
        lista.append(nome)

    idade = int(input("Digite a sua idade: "))
    if(idade < 18) or (idade > 65):
        print("IDADE INVÁLIDA")
        break
    else:
        lista.append(idade)

    salario = float(input("Digite o seu salário: "))
    if(salario <= 0):
        print("Digite um salário válido")
        break
    else:
        lista.append(salario)

    sexo = str(input("Digite seu sexo: \nM-Masculino \nF-Feminino \nO-Outro "))
    if(sexo == "M") or (sexo == "F") or (sexo == "O"):
        lista.append(sexo)
    else:
        print("Digite um sexo válido")
        break
        

    ec = str(input("Digite seu estado civíl: \nS-Solteiro \nC-Casado \nV-Viúvo \nD-Divorciado "))
    if(ec == "S") or (ec == "C") or (ec == "V") or (ec == "D"):
        lista.append(ec)
    else:
        print("Estado civil inválido")
        break
    
    print("Suas informações foram: ",lista)

