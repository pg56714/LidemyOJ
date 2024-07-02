# 題目：NM 乘法表
# https://oj.lidemy.com/problem/1024

N = int(input())
M = int(input())

for i in range(1, N+1):
    for j in range(1, M+1):
        # print(str(i) + '*' + str(j) + '=' + str((i) * (j)))
        print(i, '*', j, '=', (i * j))
