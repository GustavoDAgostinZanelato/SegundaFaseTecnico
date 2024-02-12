""" Exercício 5 """

temperatura = []
nova_temp = []


def temp_mes():

    for i in range(3):
        temp = float(input("Digite a média de temperatura do mês: "))
        temperatura.append(temp)

    temperatura.sort()
    print("A maior temperatura do ano foi de",temperatura[-1])
    print("A menor temperatura do ano foi de",temperatura[0])

    print("A ordem que as temperaturas foram informadas foi:")
    for i in temperatura:
        print(i)

    print("A ordem inversa das temperaturas é de: ")
    for i in reversed(temperatura):
        print(i)


    media = sum(temperatura)
    tamanho = len(temperatura)
    resultado = (media/tamanho)
    print("A média de temperatuas do ano foi de:",resultado)

    for i in temperatura:
        if(i > resultado):
            nova_temp.append(i)
    print("As temperatuas acima da média anual foram:",nova_temp)
 
def main():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Digite a temperatura media do mês \n2-Sair "))
        if(menu == 1):
            temp_mes()

        if(menu == 2):
            break
main()

