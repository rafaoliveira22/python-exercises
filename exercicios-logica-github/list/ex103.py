"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""

ages = [13, 13, 13, 13, 13, 13, 13, 13]
heights = [1.80, 1.76, 1.88, 1.65, 1.55, 1.87, 1.99, 1.80]

average_height = sum(heights) / len(heights)
count = 0

for key, value in enumerate(heights):
    if ages[key] > 13 and value < average_height:
        count += 1

print(f'{ages=}\n{heights=}\n')

print(f'AVERAGE HEIGHT: {average_height:.2f}')
print(f'{count} STUDENTS ARE OVER 13 YEARS OLD AND HEIGHT LESS THAN THE AVERAGE HEIGHT\nOF THESE STUDENTS')
#{count} ALUNOS TEM MAIS DE 13 ANOS E ALTURA INFERIOR A MÉDIA DE ALTURA DESSE ALUNOS


# students = [
#     {'student': 1, 'age': 18, 'height': 1.85},
# ]
