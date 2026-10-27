# #015 - Aluguel de Carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60.00 por dia e
# R$0,15 por Km rodado.

km = int(input("Informe a km: "))
dias = int(input("Informe os dias: "))
preco_final = 60 * dias + 0.15 * km

print(f"O preco final ficou em {preco_final} para {dias=} e {km=}")
