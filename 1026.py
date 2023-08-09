# 題目：判斷等比數列
# https://oj.lidemy.com/problem/1026
# 3, 6, 12, 24, 48，6/3 = 2、12/6 = 2，這些相除的值都相等，我們就稱這個等差數列的公比為 2

n = int(input())
num = (input().split(' '))


def isValid(n, num):
    if (n <= 2):
        return True

    d = int(num[1]) / int(num[0])
    for i in range(2, len(num)):
        if (int(num[i]) / int(num[i - 1]) != d):
            return False
    return True


if isValid(n, num):
    print('Yes')
else:
    print('No')
