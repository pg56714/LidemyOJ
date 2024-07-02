# 題目：完全平方和
# https://oj.lidemy.com/problem/1031
# 1、9、16、25、36、49，這些都是完全平方數
# 輸入30，輸出55，1+4+9+16+25 = 55

n = int(input())
sum = 0

for i in range(1, n + 1):
    if (i ** 2) < n:
        sum += i ** 2

print(sum)
