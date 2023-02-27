# todo: replace this with an actual task
def task_1(str):
    # Разбить предложение на слова
    words = str.split()

    # Найти длину последнего слова
    last_word_length = len(words[-1])
    return last_word_length


def task_2(str):
    # Разбить предложение на слова
    words = str.split()

    # Поменять местами четные и нечетные слова по порядку следования
    for i in range(len(words) - 1):
        if i % 2 == 0:
            words[i], words[i + 1] = words[i + 1], words[i]

    # Объединить слова обратно в предложение
    new_sentence = " ".join(words)
    return new_sentence


def task_3(str):
    words = str.split()
    count = 0
    for i in range(1, len(words)):
        prev_last_letter = words[i - 1][-1].lower()
        curr_first_letter = words[i][0].lower()

        if prev_last_letter == curr_first_letter:
            count += 1
    return count
