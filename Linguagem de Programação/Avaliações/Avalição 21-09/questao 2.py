lista_geral = []


# def pra adicionar informações de contato
def adicionar():
    print("Insira as informações que deseja salvar")
    
    nome = input("Digite o nome do contato: ")
    num_telefone = input("Digite o numero do telefone: ")
    email = input("Digite o endereco de E-Mail do seu contato: ")
    lista_secundaria = [nome, email, num_telefone]
    
    lista_geral.append(lista_secundaria)
    

# def que mostra todos os contatos exitentes
def visualizar():    
    print("Esses são os contatos que estão salvos em seu sistema: ")
    print(lista_geral)
    print("")
 

# def de edição dos contatos
def editar():
    print("Essa é a sua lista d contatos atual:")
    print(lista_geral)
    index = int(input("Digite o index correspondente ao contato que voce deseja modificar: "))
    index2 = int(input("Digite qual opçõa voce deseja modificar (0-nome, 1-telefone ou 2-e-mail): "))
    edicao = input("Insira o valor/nome da nova informação: ")
    
    lista_geral[index][index2] = edicao
    
    print(lista_geral)
 
 
# def para excluir algum contato   
def excluir():
    print("Essa é a sua lista de contatos atual:")
    print(lista_geral)
    delete = int(input("Digite o index correspondente ao contato que voce deseja excluir: "))
    del lista_geral[delete]
    print(lista_geral)
    print("")
    
    
# def com um menu para o programa
def main():
    while True:
        menu = int(input("Como deseja porsseguir: \n1-Adicionar contato \n2-Vsualizar Contatos \n3-Editar Contatos \n4-Excluir Contatos \n5-Sair "))
        
        if(menu == 5):
            break
        
        if(menu == 1):
            adicionar()
            
        elif(menu == 2):
            visualizar()
            
        elif(menu == 3):
            editar()
            
        elif(menu == 4):
            excluir()
            
        else:
            print("Digite uma opção válida \n6")


main()