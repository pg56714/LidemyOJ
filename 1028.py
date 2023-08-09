# 題目：生命靈數
# https://oj.lidemy.com/problem/1028
# 以1946-06-14為例，1+9+4+6+0+6+1+4 = 31，3+1 = 4，把每個結果的每個位數，加到剩下一位數

n = input().replace(' ', '')
# print(n)

while len(str(n)) != 1:
    sum = 0
    for i in str(n):
        sum += int(i)
    # print(sum)
    n = str(sum)

print(n)
