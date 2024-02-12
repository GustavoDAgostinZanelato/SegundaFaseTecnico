""" 23) Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os 
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou 
não continuar a escrever valores. """

lista_numeros = []

def operacao():
    while True:
        numero = int(input("Digite um valor inteiro: "))
        lista_numeros.append(numero)
        vereficacao = str(input("Deseja continuar (S/N): "))

        if(vereficacao == "S"):
            operacao()

        if(vereficacao == "N"):
            resultados()
            break
        
def resultados():
    print(lista_numeros)

    total_num = len(lista_numeros)
    soma = sum(lista_numeros)
    resultado = (soma / total_num)
    print("A média entre os valores digitados é de:",resultado)

    lista_numeros.sort()
    print("O menor valor da lista é",lista_numeros[0])
    print("O maior valor da lista é",lista_numeros[-1])
    print("")


def main ():
    while True:
        menu = int(input("Como deseja continuar: \n1-Inserir números \n2-Sair "))

        if(menu == 1):
            operacao()
        
        if(menu == 2):
            break

main()