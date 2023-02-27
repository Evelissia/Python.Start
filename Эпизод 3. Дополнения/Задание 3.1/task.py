import math

def task_1(text):
    sentences = text.split('. ')  # Разбить текст на предложения по точке и пробелу
    if sentences[-1][-1] != '.':
        sentences[-1] += '.'  # Добавить точку в конце последнего предложения, если ее нет
    word_counts = []  # Список для хранения количества слов в каждом предложении

    for sentence in sentences:
        words = sentence.split()  # Разбить предложение на слова
        word_counts.append(len(words))  # Добавить количество слов в предложении в список

    # Удалить точку из последнего предложения, если она была в исходном тексте
    if '.' in sentences[-1]:
        sentences[-1] = sentences[-1][:-1]

    result = {}  # Словарь для хранения результата
    for i in range(len(sentences)):
        result[sentences[i]] = word_counts[i]  # Сопоставить предложение с количеством слов

    return result  # Вернуть словарь с результатом



def task_2(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance