# #005 - Antecessor e Sucessor
# Faça um programa que leia um número inteiro e mostre o seu antecessor e
# sucessor.


# def teste():
#     print("teste")


# teste()
# teste()

# • int (Inteiro): Guarda números inteiros, positivos ou negativos, sem parte decimal (exemplo: 5, -10, 0).
# • float (Ponto Flutuante): Guarda números reais com casas decimais, separados por ponto (exemplo: 3.14, -0.5, 2.0).
# • str (String): Guarda textos alfanuméricos ou caracteres, delimitados por aspas simples ou duplas (exemplo: "Olá", 'Python').
# • bool (Booleano): Guarda valores lógicos de verdadeiro ou falso, escritos sempre com a primeira letra maiúscula: True ou False

# numero_inteiro = 5

# numero_string = str(numero_inteiro)

# print(numero_string, numero_inteiro)

texto_numero: str = input("Digite um número inteiro: ")

numero: int = int(texto_numero)

sucessor: int = numero + 1
antecessor: int = numero - 1

saida: str = (
    f"Numero digitado {numero}, sucessor: {sucessor} antecessor {antecessor}"
)

print(saida)
