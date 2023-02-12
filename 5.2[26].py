"""
5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
Разрешается использовать только операцию умножения.
Циклы использовать нельзя

Примеры/Тесты:
<function_name>(2,0) -> 1
<function_name>(2,1) -> 2
<function_name>(2,3) -> 8
<function_name>(2,4) -> 16
"""
def degree(base,exp):
    if exp == 1 :
        return base
    if exp != 1 :
        # return (base *degree(base, exp -1 ))
        return (pow(base, exp))
base = int(input('Введите число:'))
exp = int(input('В какую степень возвести ? :'))

print(f"Результат возведения {base} в степень {exp} равен:", degree(base, exp))