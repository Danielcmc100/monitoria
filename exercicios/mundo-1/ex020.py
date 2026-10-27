# #020 - Sorteando uma ordem na lista
# Faça um programa que leia o nome dos quatro alunos e sorteie uma ordem.

nomes_alunos: list[str] = []
for i in range(1, 5):
    nome = input(f"Aluno {i}: ")
    nomes_alunos.append(nome)
