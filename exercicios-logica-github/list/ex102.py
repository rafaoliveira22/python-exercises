"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

amount_elements = 3
A = []
B = []
C = []

D = []

for i in range(amount_elements):
    A.append(int(input(
        f'Digite o {i + 1}° número da lista A: '
    )))
    B.append(int(input(
        f'Digite o {i + 1}° número da lista B: '
    )))
    C.append(int(input(
        f'Digite o {i + 1}° número da lista C: '
    )))


    D.append(A[i])
    D.append(B[i])
    D.append(C[i])

print(f'\n{A=}\n{B=}\n{C=}\nELEMENTOS DE A,B e C INTERCALADOS: {D}')