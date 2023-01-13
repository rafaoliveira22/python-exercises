"""
Faça um programa que:

* [OK] Leia um número indeterminado de valores, correspondentes a notas;
* [OK] Encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).

Após esta entrada de dados, faça: 

* [OK] Mostre a quantidade de valores que foram lidos; 
* [OK] Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
* [OK] Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 
* [OK] Calcule e mostre a soma dos valores; 
* [OK] Calcule e mostre a média dos valores; 
* [OK] Calcule e mostre a quantidade de valores acima da média calculada; 
* [OK] Calcule e mostre a quantidade de valores abaixo de sete; 

Encerre o programa com uma mensagem;
"""

user_inputs = []
while True:
    user_input = input('TYPE IT (GRADE): ')
    if user_input == '-1': break

    try:
        user_input_float = float(user_input)
        user_inputs.append(user_input_float)
    except ValueError:
        print(f'[ERROR -> "{user_input}"]. ONLY NUMBERS\n')

length_user_inputs = len(user_inputs)
print(f'\n{length_user_inputs} GRADES HAVE BEEN READ')

sum_user_inputs = sum(user_inputs)
average_user_inputs = sum_user_inputs / length_user_inputs

# accountants
amount_inputs_above_average = 0
amount_inputs_below_average = 0

print('\nVALUES INFORMED IN ORDER')
for i in user_inputs:
    print(i, end=" ")
    
    if i > average_user_inputs:
        amount_inputs_above_average += 1
    if i < 7:
        amount_inputs_below_average += 1

print('\n\nVALUES INFORMED IN REVERSE ORDER')
index_reverse = length_user_inputs
for i in user_inputs:
    index_reverse -= 1
    print(user_inputs[index_reverse])


print(f'\n* SUM: {sum_user_inputs}')
print(f'* AVERAGE: {average_user_inputs}')
print(f'* VALUES ABOVE AVERAGE: {amount_inputs_above_average}')
print(f'* VALUES BELOW AVERAGE: {amount_inputs_below_average}')

print('\nFINISH. THANKS 😁')


