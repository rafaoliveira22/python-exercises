def somar_numeros(*args):
    return sum(args)

print(somar_numeros(2, 2, 2))
print()

"""Faça um Programa que peça dois números e imprima a soma."""
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

num1_int = int(num1)
num2_int = int(num2)
soma = num1_int + num2_int
print(f'{num1} + {num2} = {soma}')