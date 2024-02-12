import mysql.connector

#Criando a conexão com banco
conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '', #Mudar a senha
    database = 'hotel', 
)
cursor = conexao.cursor()


# Biblioteca utilizada para a formatação da data de entrada e saída da tabela "Reservas"
from datetime import datetime


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def funcionarios():

    print("\n Bem-vindo a aba de cadastro de nossos funcionários")
    print("-" * 53)

    # Cadastro do CPF
    while True:
        cpf = input("Digite o CPF do novo colaborador: ")
        num_casas_decimais = len(cpf)
        if (num_casas_decimais != 3):
            print("Valor Inválido. Tente Novamente")
        else:
            break

    # Nome do novo Colaborador
    nome = input("Insira o nome completo do colaborador: ")
    
    #Cadastro da área de atuação do funcionário
    while True: 
        cargo = input("\n Informe o cargo do novo colaborador: \n R) Recepcionista \n S) Segurança \n C) Cozinheiro ")
        if cargo != "R" and cargo != "S" and cargo != "C":
            print("Informe um cargo válido. Tente Novamente")
        else:
            break
        
    # Cadastro da Carga Horária do Colaborador
    while True:
        carga_horaria = int(input("\nQual o número de horas que o funcionário irá trabalhar? "))
        if (carga_horaria >= 12):
            print("Informe uma carga horária digna. Tente Novamente")
        else: break

    # Informando o período do dia que o funcionário irá trabalhar
    while True: 
        periodo = input("\nQual o período de trabalho do funcionário: \nM) Matutino \nV) Vespertino \nN) Noturno ")
        if periodo != "M" and periodo != "V" and periodo != "N":
            print("Período Inválido. Tente Novamente")
        else:
            break

    #Salário dos Funcionarios
    if(cargo == "R"):
        salario = 3000.00

    elif(cargo == "S"):
        salario = 4000.00

    elif(cargo == "C"):
        salario = 6000.00

    comando = f'INSERT INTO colaborador (CPF, Nome, Função, CargaHorária, Período, Salário) VALUES ({cpf}, "{nome}", "{cargo}", {carga_horaria}, "{periodo}", {salario})' 
    cursor.execute(comando)
    conexao.commit()
    
    print("\n Novo colaborador cadastrado com sucesso!")
    print("-" * 43, "\n")
    
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def reservas():

    print("\n Bem-vindo a aba de cadastro das reservas")
    print("-" * 42, "\n")

    # Cadastro do CPF
    while True:
        cpf = input("Digite o CPF do cliente: ")
        num_casas_decimais = len(cpf)
        if (num_casas_decimais != 3):
            print("Valor Inválido. Tente Novamente")
        else:
            break

    # Cadastro do Nome do Cliente
    nome = input("Informe o nome completo do cliente: ")
    
    #Data de entrada dos reservistas
    data_entrada = input("Informe a data de entrada do reservista: ")
    data1_obj = datetime.strptime(data_entrada, '%d/%m/%Y')

    #Data de saída dos reservistas
    data_saida = input("Informe a data de saída do reservista: ")
    data2_obj = datetime.strptime(data_saida, '%d/%m/%Y')

   # Calcula a diferença entre as datas
    diferenca = data2_obj - data1_obj

    # Obtém o número de dias como um inteiro
    dias = diferenca.days


    while True:
        tipo_quarto = int(input("Selecione o tipo de quarto desejado: \n1-Solteiro \n2-Casal \n3-Família \n"))
        if(tipo_quarto > 3) and (tipo_quarto < 1):
            print("Informe uma opção de quarto válida. Tente Novamente")
        else:
            break

    #Selecionar o número do quarto disponível
    while True:

        if(tipo_quarto == 1):

            #Verificando quartos ocupados
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            
            quartos = []
            for i in range(len(resultado)):
                    quartos.append(resultado[i][0])
                   

            comando2 = 'SELECT * FROM reserva'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando2)
            resultado2 = cursor.fetchall()  # Lendo o banco de dados
            
            reserva = []
            for i in range(len(resultado2)):
                reserva.append(resultado2[i][4])

            lista3 = list(filter(lambda x: x not in reserva, quartos))


            #Escolha do quarto
            print("")
            valores_novos = [valor for valor in lista3 if valor < 200]
            print("Quartos disponíveis: ", valores_novos)
            numero = int(input("Digite o número do quarto desejado: ")) 

            if numero in lista3:
                print("\n O quarto", numero, "está disponível.")
                break  
            else:
                print("\n O quarto", numero, "á está ocupado. Escolha outro.")
                

        elif(tipo_quarto == 2):

             #Verificando quartos ocupados
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            
            quartos = []
            for i in range(len(resultado)):
                    quartos.append(resultado[i][0])
                   

            comando2 = 'SELECT * FROM reserva'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando2)
            resultado2 = cursor.fetchall()  # Lendo o banco de dados
            
            reserva = []
            for i in range(len(resultado2)):
                reserva.append(resultado2[i][4])

            lista3 = list(filter(lambda x: x not in reserva, quartos))


            #Escolha do quarto
            print("")
            valores_novos = [valor for valor in lista3 if 200 <= valor <= 300]
            print("Quartos disponíveis: ", valores_novos)
            numero = int(input("Digite o número do quarto desejado: ")) 

            if numero in lista3:
                print("\n O quarto", numero, "está disponível.")
                break  
            else:
                print("\n O quarto", numero, "á está ocupado. Escolha outro.")
                

        elif(tipo_quarto == 3):

                #Verificando quartos ocupados
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            
            quartos = []
            for i in range(len(resultado)):
                    quartos.append(resultado[i][0])
                   

            comando2 = 'SELECT * FROM reserva'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando2)
            resultado2 = cursor.fetchall()  # Lendo o banco de dados
            
            reserva = []
            for i in range(len(resultado2)):
                reserva.append(resultado2[i][4])

            lista3 = list(filter(lambda x: x not in reserva, quartos))


            #Escolha do quarto
            print("")
            valores_novos = [valor for valor in lista3 if 300 <= valor <= 400]
            print("Quartos disponíveis: ", valores_novos)
            numero = int(input("Digite o número do quarto desejado: ")) 

            if numero in lista3:
                print("\n O quarto", numero, "está disponível.")
                break  
            else:
                print("\n O quarto", numero, "á está ocupado. Escolha outro.")
            


    # Determinando o valor do quarto
    if(tipo_quarto == 1):
        valor = 400
    elif(tipo_quarto == 2):
        valor = 800
    elif(tipo_quarto == 3):
        valor = 1200
    
    valor_final = valor * dias

     
    comando = f'INSERT INTO reserva (CPF, Nome, DataEntrada, DataSaída, Quarto, Valor) VALUES ({cpf}, "{nome}", "{data2_obj}", "{data1_obj}", {numero}, {valor_final})' 
    cursor.execute(comando)
    conexao.commit()
    
    print("\n Nova reserva cadastrada com sucesso!")
    print("-" * 39, "\n")
     

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def quartos():
    
    print("\n Bem-vindo a aba de cadastro dos quartos")
    print("-" * 42, "\n")
    
    #Selecionar o tipo do quarto desejado
    while True:
        tipo_quarto = int(input("Selecione o tipo de quarto desejado: \n1-Solteiro \n2-Casal \n3-Família \n"))
        if(tipo_quarto > 3) and (tipo_quarto < 1):
            print("Informe uma opção de quarto válida. Tente Novamente")
        else:
            break


    #Selecionar o número do quarto disponível
    while True:

        if(tipo_quarto == 1):

            #Verificando quartos já cadastrados
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            
            quartos_disponiveis = []
            for i in range(len(resultado)):
                numero_quarto = resultado[i][0]
                if numero_quarto < 200:
                    quartos_disponiveis.append(resultado[i][0])

            #Escolha do quarto
            print("")
            print("Números dos quartos já cadastrados: ", quartos_disponiveis)
            numero = int(input("Digite número do novo quarto: ")) 

           
            if numero in quartos_disponiveis:
                print("\n O quarto", numero, "já está cadastrado. Escolha outro.")
                
            else:
                print("\n O quarto", numero, "está disponível.")
                break  
                

        elif(tipo_quarto == 2):

            #Verificando quartos já cadastrados
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            
            quartos_disponiveis = []
            for i in range(len(resultado)):
                numero_quarto = resultado[i][0]
                if numero_quarto < 300 and numero_quarto > 200:
                    quartos_disponiveis.append(resultado[i][0])

            #Escolha do quarto
            print("")
            print("Números de quartos já cadastrados: ", quartos_disponiveis)
            numero = int(input("Digite número do novo quarto: ")) 

           
            if numero in quartos_disponiveis:
                print("\n O quarto", numero, "já está cadastrado. Escolha outro.")
                
            else:
                print("\n O quarto", numero, "está disponível.")
                break  
                
        
        elif(tipo_quarto == 3):

            #Verificando quartos já cadastrados
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            
            quartos_disponiveis = []
            for i in range(len(resultado)):
                numero_quarto = resultado[i][0]
                if numero_quarto < 400 and  numero_quarto > 300:
                    quartos_disponiveis.append(resultado[i][0])

            #Escolha do quarto
            print("")
            print("Números de quartos já cadastrados: ", quartos_disponiveis)
            numero = int(input("Digite número do novo quarto: ")) 

           
            if numero in quartos_disponiveis:
                print("\n O quarto", numero, "já está cadastrado. Escolha outro.")
                
            else:
                print("\n O quarto", numero, "está disponível.")
                break  


    # Determinando o valor do quarto
    if(tipo_quarto == 1):
        valor = 400
    elif(tipo_quarto == 2):
        valor = 800
    elif(tipo_quarto == 3):
        valor = 1200


    comando = f'INSERT INTO quartos (Número, Tipo, Valor) VALUES ({numero}, {tipo_quarto}, {valor})' 
    cursor.execute(comando)
    conexao.commit()
    
    print("\n Novo quarto cadastrado com sucesso!")
    print("-" * 37, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def visualizar():
    
    print("")
    tabela = int(input("Escolha a tabela para visualizar: \n1-Colaborador \n2-Quartos \n3-Reservas \n4-Voltar \n"))
    
    if(tabela == 4):
        print("")
        main()
    
    #Selecionando a tabela Colaborador
    if(tabela == 1):
        print("")
        comando = f'SELECT * FROM colaborador'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
            print('-' * 92)
        print("")
        visualizar()
    
    #Selecionando a tabela Quartos
    elif(tabela == 2):
        print("")
        comando = f'SELECT * FROM quartos'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"Número: {i[0]}    Tipo: {i[1]}    Valor: {i[2]}")
            print('-' * 40)
        print("")
        visualizar()
    
    #Selecionando a tabela Reservas
    elif(tabela == 3):
        print("")
        comando = f'SELECT * FROM reserva'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
            print('-' * 112)
        print("")
        visualizar()
        
       
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def deletar():
    
    print("")
    menu_deletar = int(input("Como deseja proseguir: \n1-Excluir Quarto \n2-Excluir Funcionário \n3-Excluir Reserva \n4-Voltar "))

    if(menu_deletar == 4):
        print("")
        main()

    if(menu_deletar == 1):
        print("")
        comando = f'SELECT * FROM quartos'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"Número: {i[0]}    Tipo: {i[1]}    Valor: {i[2]}")
            print('-' * 40)
        print("")
        numero = int(input("Qual é o número do quarto que deseja excluir: "))
        comando = f'DELETE FROM quartos WHERE Número = "{numero}"'
        cursor.execute(comando)
        conexao.commit()
        print("")
        comando = f'SELECT * FROM quartos'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"Número: {i[0]}    Tipo: {i[1]}    Valor: {i[2]}")
            print('-' * 40)
        print("")


    elif(menu_deletar == 2):
        print("")
        comando = f'SELECT * FROM colaborador'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
            print('-' * 92)
        print("")
        numero = int(input("Qual é o número do CPF do funcionário que deseja excluir: "))
        comando = f'DELETE FROM colaborador WHERE CPF = "{numero}"'
        cursor.execute(comando)
        conexao.commit()
        print("")
        comando = f'SELECT * FROM colaborador'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
            print('-' * 92)
        print("")

    
    elif(menu_deletar == 3):
        print("")
        comando = f'SELECT * FROM reserva'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
            print('-' * 112)
        print("")
        numero = int(input("Qual é o número do CPF do reservista que deseja excluir: "))
        comando = f'DELETE FROM reserva WHERE CPF = "{numero}"'
        cursor.execute(comando)
        conexao.commit()
        print("")
        comando = f'SELECT * FROM reserva'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
            print('-' * 112)
        print("")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def editar():

    print("")
    menu_editar = int(input("Como deseja proseguir: \n1-Editar Quarto \n2-Editar Funcionário \n3-Editar Reserva \n4-Voltar "))

    if(menu_editar == 4):
        print("")
        main()

    

    if(menu_editar == 1):
        print("")
        comando = f'SELECT * FROM quartos'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"Número: {i[0]}    Tipo: {i[1]}    Valor: {i[2]}")
            print('-' * 40)
        print("")

        localizar_quarto = int(input("Qual é o número do quarto que deseja atualizar os dados: "))
        sub_menu = int(input("Qual item deseja editar: \n1-Número \n2-Tipo \n3-Valor \n"))

        if(sub_menu == 1):
            print("")
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            
            quartos_disponiveis = []
            for i in range(len(resultado)):
                numero_quarto = resultado[i][0]
                quartos_disponiveis.append(resultado[i][0])

            #Escolha do quarto
            print("")
            print("Números dos quartos já cadastrados: ", quartos_disponiveis)
            numero = int(input("Digite número do novo quarto: ")) 

            if numero in quartos_disponiveis:
                print("\n O quarto", numero, "já está cadastrado. Escolha outro.")
                
            else:
                print("\n O quarto", numero, "está disponível.")
                comando = f'UPDATE quartos SET Número = {numero} WHERE Número = {localizar_quarto}'
                cursor.execute(comando)
                conexao.commit()
                print("")
                comando = f'SELECT * FROM quartos'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                for i in resultado:
                    print(f"Número: {i[0]}    Tipo: {i[1]}    Valor: {i[2]}")
                    print('-' * 40)
                print("")
                editar()
            editar()
        
        elif(sub_menu == 2):
            print("")
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            while True:
                tipo_quarto = int(input("Selecione o tipo de quarto desejado: \n1-Solteiro \n2-Casal \n3-Família \n"))
                if(tipo_quarto > 3) or (tipo_quarto < 1):
                    print("Informe uma opção de quarto válida. Tente Novamente")
                else:
                    comando = f'UPDATE quartos SET Tipo ={tipo_quarto} WHERE Número = {localizar_quarto}'
                    cursor.execute(comando)
                    conexao.commit()
                    print("")
                    comando = f'SELECT * FROM quartos'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(f"Número: {i[0]}    Tipo: {i[1]}    Valor: {i[2]}")
                        print('-' * 40)
                    print("")
                    break
        
        elif(sub_menu == 3):
            print("")
            comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
            cursor.execute(comando)
            resultado = cursor.fetchall()  # Lendo o banco de dados
            while True:
                valor = int(input("Digite o novo valor para o quarto: "))
                if(valor < 0):
                    print("Digite um valor válido. Tente Novamente")
                else:
                    comando = f'UPDATE quartos SET Valor ={valor} WHERE Número = {localizar_quarto}'
                    cursor.execute(comando)
                    conexao.commit()
                    print("")
                    comando = f'SELECT * FROM quartos'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(f"Número: {i[0]}    Tipo: {i[1]}    Valor: {i[2]}")
                        print('-' * 40)
                    print("")
                    break



    elif(menu_editar == 2):
        print("")
        comando = f'SELECT * FROM colaborador'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
            print('-' * 92)
        print("")

        localizar_funcionario = int(input("Qual é o CPF do funcionário que deseja atualizar os dados: "))
        sub_menu = int(input("Qual item deseja editar: \n1-CPF \n2-Nome \n3-Função \n4-Carga Horária \n5-Período \n6-Salário \n"))

        if(sub_menu == 1):
            print("")
            while True:
                cpf = input("Digite o CPF do novo colaborador: ")
                num_casas_decimais = len(cpf)
                if (num_casas_decimais != 3):
                    print("Valor Inválido. Tente Novamente")
                else:
                    break
            comando = f'UPDATE colaborador SET CPF= {cpf} WHERE CPF = {localizar_funcionario}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM colaborador'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
                print('-' * 92)
            print("")
            editar()

        elif(sub_menu == 2):
            print("")
            nome = input("Insira o novo Nome do funcionário: ")
            comando = f'UPDATE colaborador SET Nome= "{nome}" WHERE CPF = {localizar_funcionario}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM colaborador'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
                print('-' * 92)
            print("")
            editar()

        elif(sub_menu == 3):
            print("")
            while True: 
                cargo = input("\n Informe o cargo do novo colaborador: \n R) Recepcionista \n S) Segurança \n C) Cozinheiro ")
                if cargo != "R" and cargo != "S" and cargo != "C":
                    print("Informe um cargo válido. Tente Novamente")
                else:
                    break
            comando = f'UPDATE colaborador SET Função = "{cargo}" WHERE CPF = {localizar_funcionario}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM colaborador'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
                print('-' * 92)
            print("")
            editar()


        elif(sub_menu == 4):
            print("")
            while True:
                carga_horaria = int(input("\nQual o número de horas que o funcionário irá trabalhar? "))
                if (carga_horaria >= 12):
                    print("Informe uma carga horária digna. Tente Novamente")
                else: break
            comando = f'UPDATE colaborador SET CargaHorária = "{carga_horaria}" WHERE CPF = {localizar_funcionario}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM colaborador'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
                print('-' * 92)
            print("")
            editar()


        elif(sub_menu == 5):
            print("")
            while True: 
                periodo = input("\nQual o período de trabalho do funcionário: \nM) Matutino \nV) Vespertino \nN) Noturno ")
                if periodo != "M" and periodo != "V" and periodo != "N":
                    print("Período Inválido. Tente Novamente")
                else:
                    break
            comando = f'UPDATE colaborador SET Período = "{periodo}" WHERE CPF = {localizar_funcionario}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM colaborador'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
                print('-' * 92)
            print("")
            editar()


        elif(sub_menu == 6):
            print("")
            salario = int(input("Digite o novo salário do funcionário: "))
            comando = f'UPDATE colaborador SET Salário = "{salario}" WHERE CPF = {localizar_funcionario}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM colaborador'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Função: {i[2]}    Carga Horária: {i[3]}    Período: {i[4]}    Salário: {i[5]}")
                print('-' * 92)
            print("")
            editar()
    

    elif(menu_editar == 3):
        print("")
        comando = f'SELECT * FROM reserva'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
            print('-' * 112)
        print("")

        localizar_reserva = int(input("Qual é o CPF do reservista que deseja atualizar os dados: "))
        sub_menu = int(input("Qual item deseja editar: \n1-CPF \n2-Nome \n3-Data Entrada \n4-Data Saída \n5-Quarto \n6-Valor \n"))

        if(sub_menu == 1):
            while True:
                cpf = input("Digite o CPF do cliente: ")
                num_casas_decimais = len(cpf)
                if (num_casas_decimais != 3):
                    print("Valor Inválido. Tente Novamente")
                else:
                    comando = f'UPDATE reserva SET CPF = "{cpf}" WHERE CPF = {localizar_reserva}'
                    cursor.execute(comando)
                    conexao.commit()
                    print("")
                    comando = f'SELECT * FROM reserva'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
                        print('-' * 112)
                    print("")
                    break
                editar()

        elif(sub_menu == 2):
            nome = input("Informe o novo nome completo do cliente: ")
            comando = f'UPDATE reserva SET Nome = "{nome}" WHERE CPF = {localizar_reserva}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM reserva'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
                print('-' * 112)
            print("")

        elif(sub_menu == 3):
            data_entrada = input("Informe a data de entrada do reservista: ")
            data1_obj = datetime.strptime(data_entrada, '%d/%m/%Y')
            comando = f'UPDATE reserva SET DataEntrada = "{data1_obj}" WHERE CPF = {localizar_reserva}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM reserva'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
                print('-' * 112)
            print("")

        elif(sub_menu == 4):
            data_saida = input("Informe a data de saída do reservista: ")
            data2_obj = datetime.strptime(data_saida, '%d/%m/%Y')
            comando = f'UPDATE reserva SET DataSaída = "{data2_obj}" WHERE CPF = {localizar_reserva}'
            cursor.execute(comando)
            conexao.commit()
            print("")
            comando = f'SELECT * FROM reserva'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
                print('-' * 112)
            print("")

        elif(sub_menu == 5):
            while True:
                comando = 'SELECT * FROM quartos'  # Selecionando tudo da tabela "quartos"
                cursor.execute(comando)
                resultado = cursor.fetchall()  # Lendo o banco de dados
                
                quartos = []
                for i in range(len(resultado)):
                        quartos.append(resultado[i][0])
                    

                comando2 = 'SELECT * FROM reserva'  # Selecionando tudo da tabela "quartos"
                cursor.execute(comando2)
                resultado2 = cursor.fetchall()  # Lendo o banco de dados
                
                reserva = []
                for i in range(len(resultado2)):
                    reserva.append(resultado2[i][4])

                lista3 = list(filter(lambda x: x not in reserva, quartos))


                #Escolha do quarto
                print("")
                valores_novos = [valor for valor in lista3]
                print("Quartos disponíveis: ", valores_novos)
                numero = int(input("Digite o número do quarto desejado: ")) 

                if numero in lista3:
                    print("\n O quarto", numero, "está disponível.")
                    comando = f'UPDATE reserva SET Quarto = {numero} WHERE CPF = {localizar_reserva}'
                    cursor.execute(comando)
                    conexao.commit()
                    print("")
                    comando = f'SELECT * FROM reserva'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
                        print('-' * 112)
                    print("")
                    break
                  
                else:
                    print("\n O quarto", numero, "á está ocupado. Escolha outro.")


        elif(sub_menu == 6):
            while True:
                valor = int(input("Digite o novo valor para a reserva: "))
                if(valor < 0):
                    print("Digite um valor válido. Tente Novamente")
                else:
                    comando = f'UPDATE reserva SET Valor = {valor} WHERE CPF = {localizar_reserva}'
                    cursor.execute(comando)
                    conexao.commit()
                    print("")
                    comando = f'SELECT * FROM reserva'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()
                    for i in resultado:
                        print(f"CPF: {i[0]}    Nome: {i[1]}    Data Entrada: {i[2]}    Data Saída: {i[3]}    Quarto: {i[4]}    Valor: {i[5]}")
                        print('-' * 112)
                    print("")
                    break


 # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        
        
# Menu para a edição das tabelas SQL
def main():
    
    while True:
        menu = int(input("Como deseja proseguir: \n1-Adicionar Informação \n2-Visualizar Tabelas \n3-Editar Tabelas \n4-Deletar \n5-Sair do Programa \n"))

        if(menu == 5):
            break

        if(menu == 1):
            print("")
            
            sub_menu = int(input("Como deseja proseguir: \n1-Cadastrar Funcionário do Hotel \n2-Registro de Reservas \n3-Cadastro de Quartos \n4-Voltar "))
            if(sub_menu == 4):
                print("")
                main()
            if(sub_menu == 1):
                funcionarios()
            elif(sub_menu == 2):
                reservas()
            elif(sub_menu == 3):
                quartos()

        elif(menu == 2):
            visualizar()
            
        elif(menu == 3):
            editar()
        
        elif(menu == 4):
            deletar()

main()