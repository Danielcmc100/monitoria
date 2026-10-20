# #012 - Calculando Descontos
# Faça um algoritmo que leia um e mostre o preço e calcule um desconte de 5%
# do produto.

preco = 100

desconto = 10

valor_desconto = preco * desconto / 100
valor_descontado = preco - valor_desconto

mensagem = (
    f"{preco=} com {desconto=}% sai {valor_descontado} {valor_desconto=}"
)

print(mensagem)
