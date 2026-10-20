# #009 - Tabuada
# Faça um programa que leia um número inteiro e mostre sua tabuada.

numero_text = input("digite um numero para tabuada: ")

numero = int(numero_text)

# resultado = [x * 2 for x in range(numero)]

for i in range(11):
    resultado = numero * i
    mensagem = f"{i} X {numero} = {resultado}"
    print(mensagem)
