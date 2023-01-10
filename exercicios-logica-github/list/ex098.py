"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
numbers = []
multiplication_numbers_list = 1
sum_numbers_list = 0
for _ in range(5):
    num = input('Digite um número inteiro: ')
    num_int = int(num)
    numbers.append(num_int)

    sum_numbers_list = sum(numbers)
    # or sum_numbers_list += num_int
    multiplication_numbers_list *= num_int

print(f'{numbers}\nSOMA: {sum_numbers_list}\nMULTIPLICAÇÃO: {multiplication_numbers_list}')


