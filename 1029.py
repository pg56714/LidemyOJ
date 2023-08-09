# 題目：加減乘除
# https://oj.lidemy.com/problem/1029
# 給兩個數字以及一個運算符號（只會是加減乘除其中一個），請你求出計算結果，保證數字的結果都會是整數

n = input().split(' ')
a = int(n[0])
operate = n[1]
b = int(n[2])
ans = 0

if operate == '+':
    ans = a + b
elif operate == '-':
    ans = a - b
elif operate == '*':
    ans = a * b
elif operate == '/':
    ans = a / b

print(int(ans))
