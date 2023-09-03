""" 25) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do 
usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

while True:
    nome = str(input("Digite o seu nome de usuário: "))
    senha = input("Crie uma senha: ")

    if(senha == nome):
        print("Sua senha não pode ser igual ao nome de usuário")
    else:
        print("")
        print("Informações Cadastradas \nNome:",nome,"\nSenha:",senha)
        break
