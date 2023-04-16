# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

user_size_list = int(input('Введите размер списка: '))
user_list = [random.randint(0, 5) for i in range(user_size_list)]
print(user_list)
user_number = int(input('Какое число будем искать: '))
if user_list.count(user_number) > 0:
    print(f'{user_number} встречается {user_list.count(user_number)} раз')
else:
    print('Такого символа нет')
