"""
7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
Если ритм есть, функция возвращает True, иначе возвращает False

Примеры/Тесты:
    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True
"""

def rhythm_check(text):
    phrases = text.split()
    syllable_dict = {}
    for phrase in phrases:
        syllables = sum(1 for letter in phrase if letter.lower() in "аеёиоуыэюя")
        if syllables not in syllable_dict:
            syllable_dict[syllables] = 0
        syllable_dict[syllables] += 1
    return len(syllable_dict) == 1
    if len(syllable_dict) > 1 : return False
    else:
        return True

text = input("Введите кричалку Винни_Пуха:")
print(rhythm_check(text))

