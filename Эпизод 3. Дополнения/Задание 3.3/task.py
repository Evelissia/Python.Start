def task_1(lst):
    count_dict = {}
    max_count = 0
    max_num = None
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        if count_dict[num] > max_count:
            max_count = count_dict[num]
            max_num = num
    return max_num

def task_2(X, Y):
    for i in range(8):
        for j in range(i+1, 8):
            if X[i] == X[j] or Y[i] == Y[j] or abs(X[i]-X[j]) == abs(Y[i]-Y[j]):
                return "YES"
    return "NO"

def task_3(x, y, xc, yc, r):
    if ((x - xc) ** 2 + (y - yc) ** 2) <= r ** 2:
        return True
    else:
        return False


def task_4(nums):
    count = 0
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            count += 1
    return count



def task_5(key):
    with open('file.txt', 'r') as f:
        text = f.readlines()

    encrypted_text = []
    for line in text:
        line = line.strip()  # удаляем символы переноса строки и пробелы в начале и конце строки
        encrypted_line = ''
        for char in line:
            if char.isalpha():
                if char.isupper():
                    encrypted_line += chr((ord(char) - 65 + key) % 26 + 65)
                else:
                    encrypted_line += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                encrypted_line += "b"
        encrypted_text.append(encrypted_line.lower())

    with open('encrypted_file.txt', 'w') as f:
        f.writelines(encrypted_text)

    return encrypted_text
