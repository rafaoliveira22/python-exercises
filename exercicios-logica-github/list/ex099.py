"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""

ages = []
heights = []

for _ in range(5):
    age = input('Idade: ')
    height = input('Altura: ')
    print()
    ages.append(age)
    heights.append(height)

print(f'IDADES: {ages}\nALTURAS: {heights}\n')
length_list = len(ages)
for i in ages:
    length_list -= 1
    print(f'IDADE: {ages[length_list]} ALTURA: {heights[length_list]}')