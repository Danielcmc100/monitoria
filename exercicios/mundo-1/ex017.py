# #017 - Catetos e Hipotenusa
# Faça um programa que leia o cateto oposte e adjacente de um triângulo
# retângulo, calcule o comprimento da hipotenusa.

from math import sqrt

cateto_oposto = float(input("Cateto oposto: "))
cateto_adjacente = float(input("Cateto adjacente: "))

hipotenusa = sqrt(
    cateto_oposto**2 + cateto_adjacente**2
)  # ou multiplicar por 1/2

print(f"{hipotenusa}")
