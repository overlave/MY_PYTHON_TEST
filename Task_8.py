# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input('Сколько долек по горизонтали:'))
m = int(input('Сколько долек по вертикали:'))
k = int(input('Сколько долек хочешь съесть :'))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Можно')
else:
    print('Нельзя')
