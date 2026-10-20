# #007 - Média Aritmética
# Desenvolva um programa que leia duas notas do aluno e faça uma média

nota_1_texto = input("Digite a nota 1: ")
nota_2_texto = input("Digite a nota 2: ")

nota_1 = float(nota_1_texto)
nota_2 = float(nota_2_texto)

media = nota_1 + nota_2 / 2

# notas = (nota_1, nota_2)

# media = sum(notas) / len(notas)

mensagem = f"{media=}"

print(mensagem)
