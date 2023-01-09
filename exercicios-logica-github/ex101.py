"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
"""

amount_elements = 10
A = []
B = []
C = []

for i in range(amount_elements):
    A.append(int(input(
        f'Digite o {i + 1}° número da lista A: '
    )))
    B.append(int(input(
        f'Digite o {i + 1}° número da lista B: '
    )))

    C.append(A[i])
    C.append(B[i])

print(f'\n{A=}\n{B=}\nELEMENTOS DE A E B INTERCALADOS: {C}')