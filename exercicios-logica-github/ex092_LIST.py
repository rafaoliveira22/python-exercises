"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
list_ints = []
while len(list_ints) < 5:
    num_int = int(input('Digite um número inteiro: '))
    list_ints.append(num_int)

for i in list_ints:
    print(i)