# #019 - Sorteando um item na lista
# Um professor quer sortear um dos quatro alunos. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import shuffle

nomes_alunos: list[str] = []
for i in range(1, 5):
    nome = input(f"Aluno {i}: ")
    nomes_alunos.append(nome)

shuffle(nomes_alunos)

print(f"Aluno escolhido foi: {nomes_alunos=}")
