# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

UserValue = int(input('Введите трехзначное число: '))
FirstDigit = UserValue//100
SecondDigit = (UserValue//10)%10
ThirdDigit = UserValue%10
print(FirstDigit, SecondDigit, ThirdDigit)
SumDigits = FirstDigit + SecondDigit+ThirdDigit
print(f'Сумма цифр в Вашем числе {UserValue} равна {SumDigits} ({FirstDigit} + {SecondDigit} + {ThirdDigit})')

