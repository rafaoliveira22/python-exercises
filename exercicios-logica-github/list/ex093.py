"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

list_reals = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10]
length_list = len(list_reals)

for i in list_reals:
    length_list -= 1
    print(list_reals[length_list])

# MÉTODO REVERSE
# list_reals.reverse()
# print(list_reals)

# FATIAMENTO DE LISTA
# list_reverse = list_reals[::-1]
# print(list_reverse)