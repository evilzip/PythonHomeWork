# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power_by_recursion(base: int, power: int) -> int:
    if power==0:
        return 1
    elif power ==1:
        return base
    else:
        return base*power_by_recursion(base, power-1)


base_input = int(input('Основание степени: '))
power_input = int(input('Показатель степени: '))
print(f'{base_input} в степени {power_input} = {power_by_recursion(base_input,power_input)}')