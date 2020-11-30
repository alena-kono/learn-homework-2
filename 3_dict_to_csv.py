import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
EMPLOYEES = [
    {'name': 'Bob', 'age': 24, 'job': 'driver'},
    {'name': 'Eugenia', 'age': 33, 'job': 'manager'},
    {'name': 'Nick', 'age': 18, 'job': 'sales assistant'},
    {'name': 'Lora', 'age': 29, 'job': 'accountant'}
]


def main():
    with open('employees.csv', 'w', newline='') as employees_file:
        fields = list(EMPLOYEES[0].keys())
        writer = csv.DictWriter(employees_file, fields, delimiter=';')
        writer.writeheader()
        for employee in EMPLOYEES:
            writer.writerow(employee)


if __name__ == '__main__':
    main()
