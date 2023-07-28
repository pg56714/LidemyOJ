# 題目：數字比大小
# https://oj.lidemy.com/problem/1002

import sys
ans = []

while True:
    str = sys.stdin.readline().strip('\n')
    tmp = str.split()

    a = int(tmp[0])
    b = int(tmp[1])

    if (a == 0 and b == 0):
        break
    else:
        if (a >= b):
            ans.append(a)
        else:
            ans.append(b)

for answer in ans:
    print(answer)
