# #016 - Quebrando um número
# Crie um programa que leia um número real e mostre na tela a sua porção
# inteira. Ex: digito 5.2453 e a saida é 5.

valor_texto = input("Digite o valor: ")
valor_float = float(valor_texto)
valor = int(valor_float)

# round(valor_float, ndigits=0) arredonda, não é o que queremos


print(f"{valor=}")
