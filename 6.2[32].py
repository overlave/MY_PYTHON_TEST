# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.
# 284: 1, 2, 4, 71 и 142, — их сумма равна 220.
# Первые пары дружественных чисел:
# 220, 284; 1184, 1210; 2620, 2924; 5020, 5564; 6232, 6368
#
# Для заданного числа number выведите все пары дружественных чисел, каждое из которых не превосходит number.
# Напишите функцию:
# Аргументы: целое число
# Печатает все пары дружественных чисел, не превосходящих аргумент.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
#
# Примечание:
# 1. Выделите значимые куски алгоритма и оформите их в виде функций
# 2. Задокументируйте созданные функции
# 3. Используйте type hinting
#
# Примеры/Тесты:
# <function_name>(300)
# 220 284
# <function_name>(10000)
# 220 284
# 1184 1210
# 2620 2924
# 5020 5564

"""
def sum_divisor(a: int) -> int:
"""
"""
sum_a = 0
for i in range(1, a):
if a % i == 0:
sum_a += i
return sum_a

def para_numbers(n: int) -> None:

for i in range(1, n):
sum_1 = sum_divisor(i)
sum_2 = sum_divisor(sum_1)

if i == sum_2 and i < sum_1:
print(i, sum_1)


para_numbers(10000)
"""

def sum_of_divisors(number: int) -> int:
    """Находит сумму всех делителей числа, кроме самого числа."""
    divisors_sum = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    return divisors_sum

def find_friendly_pairs(number: int) -> None:
    """Находит и выводит все пары дружественных чисел, не превосходящие заданное число."""
    friendly_pairs = set()
    for n in range(2, number):
        m = sum_of_divisors(n)
        if n < m <= number and sum_of_divisors(m) == n:
            friendly_pairs.add((n, m))
    for pair in friendly_pairs:
        print(f"{pair[0]} {pair[1]}")

# Примеры использования функции find_friendly_pairs:
find_friendly_pairs(300)
find_friendly_pairs(10000)

# Функция sum_of_divisors находит сумму всех делителей числа, кроме самого числа, используя перебор от 2 до корня из числа.
# Это дает асимптотику O(sqrt(n)).
#
# Функция find_friendly_pairs перебирает все числа от 2 до заданного числа number.
# каждого числа n находится сумма его делителей m с помощью функции sum_of_divisors.
# Если n < m <= number и сумма делителей числа m равна n, то пара (n, m) добавляется в множество friendly_pairs.
# Наконец, все пары выводятся на экран. Функция find_friendly_pairs имеет асимптотику O(n*sqrt(n)).