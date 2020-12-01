from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
task = 'Дан список учеников, нужно посчитать количество повторений каждого имени ученика.'
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
print('*' * 80, task, sep='\n')

names = [student['first_name'] for student in students]
names_counted = Counter(names)
for name, frequency in names_counted.items():
    print(f'{name}: {frequency}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
task = 'Дан список учеников, нужно вывести самое часто повторящееся имя.'
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# Пример вывода:
# Самое частое имя среди учеников: Маша
print('*' * 80, task, sep='\n')

names = [student['first_name'] for student in students]
most_frequent_name = Counter(names).most_common(1)
print(f'The most frequent name: {most_frequent_name[0][0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
task = 'Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.'
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('*' * 80, task, sep='\n')

for index, grade in enumerate(school_students, start=1):
    names = [student['first_name'] for student in grade]
    most_frequent_name = Counter(names).most_common(1)
    print(
        f'The most frequent name in class {index}:',
        f'{most_frequent_name[0][0]}'
        )


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
task = 'Для каждого класса нужно вывести количество девочек и мальчиков в нём.'
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print('*' * 80, task, sep='\n')

male_count, female_count = 0, 0
for grade in school:
    for student in grade['students']:
        if is_male[student['first_name']]:
            male_count += 1
    female_count = len(grade['students']) - male_count
    print(
        f'There are {female_count} girls and {male_count} boys',
        f'in the class {grade["class"]}'
        )


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
task = 'По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.'
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print('*' * 80, task, sep='\n')

male_max_class, female_max_class = None, None
male_count, female_count, male_max, female_max = 0, 0, 0, 0

for grade in school:
    male_count, female_count = 0, 0

    for student in grade['students']:
        if is_male[student['first_name']]:
            male_count += 1
    female_count = len(grade['students']) - male_count

    if male_count > male_max:
        male_max = male_count
        male_max_class = grade['class']
    elif female_count > female_max:
        female_max = female_count
        female_max_class = grade['class']

print(
    f'Most boys in the class {male_max_class}',
    f'Most girls in the class {female_max_class}',
    sep='\n'
    )
