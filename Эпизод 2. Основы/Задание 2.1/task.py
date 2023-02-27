def task_1(N):
    fac = 1
    for i in range(2, N+1):
        fac = fac *i
    return fac


def task_2(N):
    a = 0
    b = 1
    for i in range(N-1):
        temp = b
        b +=a
        a=temp
    return a


def task_3(N):
    k = 1
    r=[]
    while k <=N:
        if N%k == 0:
            r.append(k)
            k = k+1

    return
