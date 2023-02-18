""""
6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
Программа принимает от пользователя три числа :

Первый элемент прогрессии, Разность (шаг) и Количество элементов
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

Напишите функцию

- Аргументы: три указанных параметра
- Возвращает: список элементов арифмитической прогрессии.

Примеры/Тесты:

Ввод: 7 2 5
Вывод: [7 9 11 13 15]
Ввод: 2 3 12
Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
"""

def generate_arithmetic_progression(first, diff, count):
    progression = []
    for i in range(count):
        progression.append(first + i * diff)
    return progression

first = int(input('Введите первый элемент: '))
diff = int(input('Введите шаг: '))
count = int(input('Введите кол-во элементов: '))
print(generate_arithmetic_progression(first, diff, count))
