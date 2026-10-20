# #011 - Pintando Parede
# Faça um programa que leia a largura e altura de uma parede em metros,
# qualcule a área e a quantidade de tinta necessária para pinta-lá,
# sabendo que cada litro de tinta pinta uma área de 2m^2.

altura = 2
largura = 2

area = altura * largura

tinta = area / 2

mensagem = f"com uma área de {area}m² se gasta {tinta} litros"
print(mensagem)
