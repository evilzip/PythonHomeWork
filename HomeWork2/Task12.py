# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

product = int(input('Введите произведение загаданных чисел : '))
summ = int(input('Введите сумму загаданных чисел чисел: '))
current_number = 1
is_solution = False
while current_number <= 1000:
    # print('1')
    if (product % current_number) == 0 and (product // current_number + current_number) == summ:
        print(f'Вы загадали чиcла {product // current_number} и {current_number}')
        is_solution = True
    current_number += 1
if not is_solution:
    print('Ошибка! В натуральных числах решений нет! ')
