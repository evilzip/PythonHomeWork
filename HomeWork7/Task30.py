# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input('Первый член прогрессии: '))
difference = float(input('Разность арифметической прогрессии: '))
element_amount = int(input('Количество элементов: '))

progression_list = [(lambda n: first_element + (n - 1) * difference)(n) for n in range(0, element_amount + 1)]
print(f'Ваша прогрессия: {progression_list}')
