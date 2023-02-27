def task_1(str):
    char_count = {}
    for char in str.lower():
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def task_2(list):
    unique_A = set(list)  # создание множества из списка, чтобы получить уникальные элементы
    sum_unique = sum(unique_A)
    return sum_unique


def task_3(cities):
    result = ", ".join(cities) + "."
    return result


def task_4(a, b):
    intersection = list(set(a) & set(b))
    return intersection
