import math
from typing import Any


# Пример 1
def task_1(a, d, c):
    result: float | Any = (c-(d/5)+math.sqrt(321))/(1+a*3)
    return result


# Пример 2
def task_2(a, d, c):
    res: float | Any = (math.log10(c/3)-d+25)/(a*5-1)
    return res


# Пример 3
def task_3(a, d, c):
    res = ((c/2)+math.log(d)-35)/(a*5+1)
    return res


# Пример 4
def task_4(a, d, c):
    res = (math.tan(c)+(d/32))/((a/3)+1)
    return res


# Пример 5
def task_5(a, d, c):
    res = ((c/5)-d+1)/(c+math.tan(2*a))
    return res


# Пример 6
def task_6(a, d, c):
    res = (math.sqrt(25*c)+d-3)/(d-a*a+1)
    return res


# Пример 7
def task_7(a, d, c):
    res = (5*math.log10(c)+3*d-32)/(a*a+1)
    return res


# Пример 8
def task_8(a, d, c):
    res = (c*d - math.log(4*3*a))/(c+a-1)
    return res
