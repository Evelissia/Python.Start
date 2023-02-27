# Пример 1
import math


def task_1(a, b):
    if a > b:
        x = (math.sqrt(a*b)-3)
    else:
        if a == b:
            x = math.log10(2)
        if a < b:
            x = (math.log(a*a*a+1))/b

    return x

# Пример 2
def task_2(a, b):
    if a<b:
        x = (math.tan(a/b)+1)
    else:
        if a == b:
            x = math.tan(-1)
        if a > b:
            x = (math.sqrt(a*b-5))/(a)
    return x


# Пример 3
def task_3(a, b):
    if a > b:
        x = (math.log10(a*b)+21)
    else:
        if a == b:
            x = math.tan(-5)
        if a < b:
            x = (math.log(3*(a/b)))+1
    return x


# Пример 4
def task_4(a, b):
    if a > b:
        x = math.sqrt(a*b-1)
    else:
        if a == b:
            x = math.log10(255)
        if a < b:
            x = (math.tan(a-5))/b
    return x


# Пример 5
def task_5(a, b):
    if a > b:
        x = math.log(a/b)+31
    else:
        if a == b:
            x = math.tan(-25)
        if a < b:
            x = (math.cos(a*5-1))/a
    return x


# Пример 6
def task_6(a, b):
    if a < b:
        x = math.sqrt((b/a)+1)
    else:
        if a == b:
            x = math.sqrt(25)
        if a > b:
            x = (math.log10(a*a*a-5))/(b)
    return x
