""" 20) Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se aposentar. 
As condições para aposentadoria são:
• Ter pelo menos 65 anos, 
• Ou ter trabalhado pelo menos 30 anos, 
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos. """

print("Verificação de Aposentadoria")
nome = str(input("Digite o seu nome: "))
idade = int(input("Quantos anos você tem: "))
tempo_trabalhado = int(input("Por quantos anos você trabalhou: "))

while True:

    if(idade >= 60) & (tempo_trabalhado >= 25):
        print("Você pode se aposentar devido a sua idade a anos trabalhados")
        break
    
    if(idade >= 65):
        print("Você pode se Aposentar devido a sua idade")
        break

    if((tempo_trabalhado >= 30)):
        print("Você pode se Aposentar devido ao seus anos trabalhados")
        break


