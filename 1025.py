# 題目：水仙花數
# 一個n位數的數字，每一個數字的n次方加總等於自身
# 例如:153=1的三次方+5的三次方+3的三次方
# https://oj.lidemy.com/problem/1025

n, m = map(int, input().split())


def isNarcissistic(num):
    temp = num
    sum = 0

    while temp:  # 153、15、1、0(換下一個數字)
        # 取餘數
        # 153 % 10 = 3 ** 3 = 27
        # 15 % 10 = 5 ** 3 = 125
        # 1 % 10 = 1 ** 3
        # 最後27+125+1 = 153
        # 簡單來說 % 10 就是 等於最後一數，153 % 10 = 3...等等
        n = temp % 10
        sum += n ** len(str(num))
        # print('n：', n, 'temp：', temp)

        # 取商，153 // 10 = 15、15 // 10 = 1、1 // 10 = 0
        temp //= 10

    if sum == num:
        print(num)


for j in range(n, m+1):
    isNarcissistic(j)


# 以下程式會出現 Time Limit Exceeded
# import sys
# text = sys.stdin.readline().strip('\n')
# tmp = text.split()

# for i in range(int(tmp[0]), (int(tmp[1])+1)):
#     # str(i) 等於10的時候，索引0是1，1是0，所以迴圈跑第一圈印1，第二圈印0
#     digits = [(int(digit) ** len(str(i))) for digit in str(i)]
#     # print(digits)
#     if (sum(digits) == i):
#         print(i)
