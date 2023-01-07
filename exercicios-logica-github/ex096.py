"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

list_nums = []
list_nums_pairs = []
list_nums_odd= []

while len(list_nums) < 5:
    num =  input('Número: ')
    if num.isdigit():
        num_int = int(num)
        list_nums.append(num_int)
        if num_int % 2 == 0:
            list_nums_pairs.append(num_int)
        else: list_nums_odd.append(num_int)
    else: print('apenas números')

print(f'Pares: {list_nums_pairs}')
print(f'Ímpares: {list_nums_odd}')