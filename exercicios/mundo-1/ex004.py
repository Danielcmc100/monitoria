# #004 - Dissecando uma Variável
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo
# primitivo e todas as informações possíveis sobre ela.

variavel: str = input()

print(f"Tipo {type(variavel)}")
