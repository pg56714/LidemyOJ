# 題目：判斷質數
# https://oj.lidemy.com/problem/1020

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for j in range(2, n):
            # print(j)
            if n % j == 0:
                return False
        return True


number = int(input())

for i in range(number):
    all = int(input())

    if (isPrime(all)):
        print('Prime')
    else:
        print('Composite')
