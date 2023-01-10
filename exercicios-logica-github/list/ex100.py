"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

A = [1, 2, 3, 4 ,5 ,6 , 7, 9, 10]
soma_dos_quadrados = 0

# for _ in range(10):
for num in A:
    # num_int = int(input('DIgite um  número inteiro: '))
    soma_dos_quadrados += (num ** 2)
print(f'A soma dos quadrados do vetor {A=} é\n{soma_dos_quadrados}')