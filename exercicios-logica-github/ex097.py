"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

averages = []
amount_students_approved = 0
student_average = 0
sum_grades = 0
i = 0
j = 0

while i < 4:
    j = 0
    sum_grades = 0
    print(f'NOTAS DO ALUNO {i+1}')
    print(f'{25 * "-"}')
    while j < 10:
        grade = input(f'NOTA {j+1} DO ALUNO {i+1}: ')
        if grade.isdigit():
            grade_float = float(grade)
            sum_grades += grade_float
            j += 1
        else:
            print('Apenas notas númericas.')
            # continue
    student_average = sum_grades / j
    print(f'A MÉDIA DO ALUNO {i+1} FOI: {student_average:.2f}')
    print()

    if student_average >= 7.0: 
        amount_students_approved += 1

    averages.append(student_average)
    i += 1

print()
print(f'{amount_students_approved} ALUNOS TIVERAM MÉDIA >= A 7.0')