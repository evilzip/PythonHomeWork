# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


import random

total_coins = int(input('Введите общее количество монет: '))
coins_set = []
Orel_Counter = 0
for coin in range(1, total_coins):
    coins_set.append(random.randint(0, 1))
for coin_side in coins_set:
    if coin_side == 0:
        Orel_Counter += 1
print('Набор выпавших монет (0-Орел, 1 - решка):' + f'\n{coins_set}')
if Orel_Counter < total_coins - Orel_Counter:
    print(f'Нужно перевернуть {Orel_Counter} монеток с Орлом')
elif Orel_Counter > total_coins - Orel_Counter:
    print(f'Нужно перевернуть {total_coins - Orel_Counter} монеток с Решкой')
else:
    print(f'Орлов и решек выпало поровну. Нужно перевернуть {Orel_Counter} монеток или с Орлом,или с Решкой')
