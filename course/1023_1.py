# 題目：印出聖誕樹
# https://oj.lidemy.com/problem/1023

star = int(input())

for i in range(star):
    print(' ' * (star-i-1) + '*' * (i*2+1))

for j in range(star-1):
    print(' ' * (star-1) + '|')
