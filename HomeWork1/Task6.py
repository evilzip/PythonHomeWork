# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
UserTicketNumber = input('Введите 6-ти значный номер вашего билета:')
LeftSum = int(UserTicketNumber[0])+int(UserTicketNumber[1])+int(UserTicketNumber[2])
RightSum = int(UserTicketNumber[3])+int(UserTicketNumber[4])+int(UserTicketNumber[5])
if LeftSum == RightSum:
    print('Да! Ваш билет счастливый')
else:
    print('Нет, ваш билет несчастливый :()')
