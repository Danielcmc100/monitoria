# #006 - Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz
# quadrada.

from math import sqrt

numero_texto: str = input("Digite um número:")

numero = float(numero_texto)

dobro = numero * 2
triplo = numero * 3
raiz = sqrt(numero)

mensagem = f"{dobro=} {triplo=} {raiz=}"

print(mensagem)
