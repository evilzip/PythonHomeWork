# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
m = int(input('Сколько долек на 1й стороне плтики: '))
n = int(input('Сколько долек на 2й стороне плтики: '))
k = int(input('Сколько долек вы хотите отломить: '))
if k%m==0 or k%n==0:
    print (f'Да, Вы можетe отломить {k} долек от плитки шоколада {m}X{n}')
else:
    print (f'Нет, Вы не можетe отломить {k} долек от плитки шоколада размера {m} X {n} за один разлом')
