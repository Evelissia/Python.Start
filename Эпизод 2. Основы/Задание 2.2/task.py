
# Пример 1
def task_1(A):
    sum_positive = 0

    for i in A:
        if i > 0:
            sum_positive += i

    return sum_positive



# Пример 2
def task_2(A):
    sum_a = 0
    n = len(A)
    for i in A:
        sum_a += i

    mean_a = sum_a / n
    return mean_a


# Пример 3
def task_3(A):
    mean = sum(A) / len(A)
    sum_sq_diff = sum((x - mean)**2 for x in A)
    site = (sum_sq_diff / len(A)) ** 0.5
    return site
