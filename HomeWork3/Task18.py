##
#
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

index = 0
target_number = 0
user_size_list = int(input('Введите размер списка чисел: '))
user_list = [random.randint(1, 20) for i in range(user_size_list)]
print(user_list)
user_number = int(input('Задайте ваше число: '))
if user_number < min(user_list):
    print(f'Самое близкое по значению число к {user_number}: {min(user_list)}')
elif user_number > max(user_list):
    print(f'Самое близкое по значению число к {user_number}: {max(user_list)}')
else:
    delta = abs(max(user_list) - min(user_list))
    for i in range(user_size_list):
        if user_number != user_list[i] and abs(user_number - user_list[i]) <= delta:
            target_number = user_list[i]
            delta = abs(user_number - user_list[i])
    print(f'Самое близкое по значению число к {user_number}: {target_number}')
