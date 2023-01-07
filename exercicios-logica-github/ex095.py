"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vowels = 'A E I O U'
list_caracters = []
list_consonant = []
qtd_consonant = 0
while len(list_caracters) < 10:
    caracter = input('Digite um caracter: ').upper()
    list_caracters.append(caracter)
    if caracter not in vowels: 
        qtd_consonant += 1
        list_consonant.append(caracter)
    
print(f'CONSOANTES: {list_consonant}')
print(f'Foram lidas {qtd_consonant} consoantes')


