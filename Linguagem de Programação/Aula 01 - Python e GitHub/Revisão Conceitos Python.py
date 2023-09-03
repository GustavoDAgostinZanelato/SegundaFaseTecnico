""" 
#Declarando os Tipos de Dados
a = 5 
print(type(a)) #Numero Inteiro (int)

b = "Gustavo"
print(type(b)) #String (str)

c = 8.5
print(type(c)) #Número Float

d = ()
print(type(d)) #Tupla

e = []
print(type(e)) #Lista

f = {}
print(type(f)) #Dicionário

g = 5+1j
print(type(g)) #Número complexo

h = True
print(type(h)) #Variável Booleana """



""" #Tipos de Print()
nome = "Gustavo"
idade = 16
print("Olá", nome,"você tem", idade,"anos") #1º Modelo
print("Olá" + nome + "você tem",idade,"anos") #2º Modelo. Não adiciona espaço entre as palavras e somente soma STR
print("Olá {} você tem {} anos".format(nome,idade)) #3º Modelo.
print(f"Olá {nome} você tem {idade} anos") #4º Modelo. Metodo mais simples

#Caixa de Entrada de Dados
nome = input("Digite seu nome: ")
nome2 = input("Digite seu nome: ")
nome3 = input("Qual o seu nome: ")
print(f"{nome}\n{nome2}\n{nome3}") #\n é para pular uma linha - 4º Modelo de Print

dia = 10
mes = 8
ano = 2023
print("João estava na padaria", end=", ") #A função end serve para jntas dois prints que estão em linhas diferentes
print("pois estava com fome")
print(dia,mes,ano, sep="->") #Adiciona o caracter nas aspas entre cada uma das letras
 """

""" #Criação de Listas
nomes = ["Matheus", "Marcelo", "Maria", "Mariane", "Marcos"]
print(nomes) #Exibe toda a Lista
print(nomes[4]) #Vai exibir o nome na possição 4

nomes[2] = "Joana" #Vai alterar o nome na possição 2 para "Joana"
print(nomes) """


""" #Criação de Tuplas
carros = ("gol", "golf sapão", "vectra", "cadilac", "mercedes c120")
print(carros)
print(carros[0])
#A diferença entre lista e tupla é a impossibilidade de mudar os itens dentro da tupla
#carros[0] = "bmw x6" --> #error   """  


""" #Criação de Dicionarios
peso = {"amanda": 55.6, "João": 70.6, "Arthur": 55.6}
print(peso) """

""" a = input("Digite algo: ")
print(type(a.isnumeric())) #Verifica se é um caracter numérico
print(type(a.isalpha()) #Verifica se é um texto/letra
print(type(a.isdecimal()) #Verifica se é um número decimal
print(type(a.isalnum()) #Verifica se é um número
print(type(a.islower()) #Verifica se a palavra está toda em minúsculo
print(type(a.isupper()) #Verifica se a palavra está toda em maiúsculo
print(type(a.istitle()) #Verifica se a palavra inicia com letra maiúscula
print(type(a.isspace())) #Verifica a presença de espaços vazios """


""" conta = 2371 // 5 #Retorna apenas o valor inteiro (antes de vírgula)
conta2 = 2371 % 5 # Retorna o resto da divisão de um número (resto 0 = par   resto 1 = ímpar)
conta3 = 2371 / 5 #Retorna o resultado completo, assim como na calculadora

print(conta)
print(conta2)
print(conta3)

print(round(conta2, 2)) #Casas decimais com função
print(f"{conta2:.2f}") #Casas decimais com print formatado """

a = input("Digite seu nome: ")
b = "Joaquim"
print(f"Seja bem vindo {a:20}")
print(f"Seja bem vindo {a:<20}")
print(f"Seja bem vindo {a:<20} e {b}")
print(f"Seja bem vindo {a:^20}")