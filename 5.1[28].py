'''
5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
Примеры/Тесты:
<function_name>(0,0) -> 0
<function_name>(0,2) -> 2
<function_name>(3,0) -> 3
'''
def sum(a,b):
    if a == 0 :
        return b
    if b == 0 :
        return a
    else:
        return (a +b)
a = int(input('Введите число a :'))
b = int(input('Введите число b :'))

print(f"Сумма чисел {a} и {b} равна:", sum(a, b))