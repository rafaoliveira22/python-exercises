"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro' , 'dezembro']
average_temperatures = []

# carregar as médias de cada mes
for i in months:
    while True:
        average_month = input(f'Temperatura média do mês de {i.capitalize()}: ')
        try:
            average_month_float = float(average_month)
            average_temperatures.append(average_month_float)
            break
        except ValueError:
            print('Apenas temperaturas numéricas\n')
            continue

# calcular a media anual
average_yearly = sum(average_temperatures) / len(average_temperatures)

print(f'\nA MÉDIA ANUAL FOI: {average_yearly}\n')

# verificar quais meses excederam a media anual
count = 0
for key, value in enumerate(average_temperatures):
    if value > average_yearly:
        count += 1
        print(f'{count} - {months[key].capitalize()} - {value}°C')
    

