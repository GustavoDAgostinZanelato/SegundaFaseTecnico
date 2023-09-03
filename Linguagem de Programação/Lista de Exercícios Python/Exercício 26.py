""" 26) Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres)."""

while True:
    def main():
        while True:
            nome = str(input("Digite o seu nome: "))
            if(len(nome) <= 3):
                print("Nome Inválido")
                main()
            else:
                anos()
                break

    def anos():
        while True:
            idade = int(input("Digite sua idade: "))
            if(idade <= 0) or (idade >= 150):
                print("Idade Inválida")
                anos()
            else:
                salario()
                break

    def salario():
        while True:
            dinheiro = float(input("Digite o seu salário: "))
            if(dinheiro <= 0):
                print("Salário Inválido")
                salario()
            else:
                resto()
                break

    def resto():
        sexo = str(input("Informe seu sexo: Masculino(M) ou Feminino(F): "))
        ec = str(input("Informe seu estado civil: Solteiro(S), Casado(C), Viúvo(V) ou Divorciado(D):"))
        print("Cadastro Efetuado")
        
    break       
main()