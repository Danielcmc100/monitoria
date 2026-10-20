# #010 - Conversor de Moedas
# Crie um programa que leia quanto dinheiro você têm na carteira e mostre
# quantos dólares você pode comprar.

CONTACAO = 0.2

reais_text = input("reais: ")

reais = float(reais_text)

dolares = reais * CONTACAO

mensagem = f"com {reais=} se compra {dolares=}"

print(mensagem)
