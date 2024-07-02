# 題目：印出金字塔
# https://oj.lidemy.com/problem/1022

star = int(input())

for i in range(star):
    print(' ' * (star-i-1) + '*' * (i*2+1))
