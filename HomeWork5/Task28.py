# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def summ_recursion(number_one: int, number_two: int) -> int:
    if number_two ==0:
        return number_one
    return summ_recursion(number_one+1, number_two-1)

item_one = int(input('Первое слагаемое: '))
item_two = int(input('Второе слагаемое: '))
print(f'Если к {item_one} прибавить {item_two} получим {summ_recursion(item_one, item_two)}')

## !!! P.S. Больше чем 999 + 998 не считает. Перепольнение стека