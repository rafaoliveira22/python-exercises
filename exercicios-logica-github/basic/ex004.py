"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
i = 0
soma = 0
while i < 4:
    nota = input(f'Digite a {i+1}° nota: ')
    if nota.isdigit():
        nota_float = float(nota)
        soma += nota_float
        i += 1
    else: print('Nota inválida. Apenas números')

print(f'A média bimestral é: {soma/i}')
