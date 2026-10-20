# #008 - Conversor de Medidas
# Escreva um programa que leia um valor em metros e o exiba convertidos em
# centrímetros e milímetros.

metros_text = input("digite a quantidade em metros: ")

metros = float(metros_text)
centimetros = metros * 100
milimetros = metros * 1000

mensagem = f"em {metros=} convertido em {centimetros=} {milimetros=}"

print(mensagem)
