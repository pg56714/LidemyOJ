# 題目：判斷質數
# https://oj.lidemy.com/problem/1020

number = int(input())

for i in range(number):
    isPrime = True
    all = int(input())

    if all == 1:
        isPrime = False
    elif all == 2:
        isPrime = True
    else:
        for j in range(2, all):
            # print(j)
            if all % j == 0:
                isPrime = False
                break

    if (isPrime):
        print('Prime')
    else:
        print('Composite')
