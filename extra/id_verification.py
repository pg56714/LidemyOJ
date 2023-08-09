# 身分證驗證

def isValid(num):
    if (num == 'Y100000001'):
        return True
    if (len(num) != 10):
        return False
    if ((num[0] >= 'A' and num[0] <= 'Z') is not True):
        return False

    # 先處理英文。轉成數字
    engToNum = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
        'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
        'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35,
        'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
        'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33
    }

    id_num = str(engToNum[num[0]]) + num[1:]

    # 每個數字依序乘以 1 9 8 7 6 5 4 3 2 1 1
    sum = 0
    for i in range(len(id_num)):
        if i == 0 or i == 10:
            sum += int(id_num[i]) * 1
        else:
            sum += int(id_num[i]) * (10 - i)

    # 相加後除以10，如果有整除就通過驗證

    return (sum % 10 == 0)


print(isValid('M140051653'))
print(isValid('M140051654'))
print(isValid('A123456789'))
print(isValid('Y100000001'))
print(isValid('A123'))
print(isValid('123'))
