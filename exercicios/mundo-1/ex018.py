# #018 - Seno, Cosseno e Tangente
# Faça um programa que leia um ângulo e mostre o valor de seno, cosseno
# e tangente.

from math import cos, pi, sin, tan

angulo = float(input("Informe o angulo: ")) * (pi / 180)

seno = round(sin(angulo), 2)
cosseno = round(cos(angulo), 2)
tangente = round(tan(angulo), 2)

print(f"{seno=} {cosseno=} {tangente=}")
