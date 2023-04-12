# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

limit_number = int(input('Введите натуральное число: '))
current_number = 1
list_power_two = []
while 2 ** current_number <= limit_number:
    list_power_two.append(2 ** current_number)
    current_number += 1
print(f'Список целых степеней 2, ограниченный {limit_number}:' + f'\n {list_power_two}')
