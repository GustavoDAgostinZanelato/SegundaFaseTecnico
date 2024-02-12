""" 28) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para 
cada eleitor votar e ao final mostrar o número de votos de cada candidato. """

morais = 0
huck = 0
arrascaeta = 0

num_eleitores = int(input("Digite o número de eleitores: "))

for i in range(num_eleitores):
    voto = int(input("Em qual candidado você deseja votar: \n1-Alexandre de Morais \n2-Luciano Huck \n3-Arrascaeta "))

    if(voto == 1):
        morais = morais + 1

    if(voto == 2):
        huck = huck + 1
    
    if(voto == 3):
        arrascaeta = arrascaeta + 1

print("Votos para Alexandre de Morais",morais)
print("Votos para Alexandre de Huck",huck)
print("Votos para Alexandre de Arrascaeta",arrascaeta)



