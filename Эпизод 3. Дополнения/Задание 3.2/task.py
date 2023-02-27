def task_1(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return str(mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def task_2(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True