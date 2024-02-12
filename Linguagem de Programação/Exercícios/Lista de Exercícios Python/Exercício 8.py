""" 8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a 
quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m² """

largura = float(input("Digite a largura de sua parede: "))
altura = float(input("Digite a altrua de sua parede: "))

area = (altura * largura)

print ("A área de sua parede é de ",area)

qtd_tinta = (area / 2)

print("Serão nescessários",qtd_tinta,"litros de tinta para pintar uma parede com área de",area,"m²")