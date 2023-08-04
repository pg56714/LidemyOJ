# 題目：印出聖誕樹
# https://oj.lidemy.com/problem/1023

star = int(input())


def repeat(str, n):
    result = ''
    for k in range(n):
        result += str
    return result


for i in range(star):
    print(str(repeat(' ', star-i-1)) + str(repeat('*', (i*2+1))))

for j in range(star-1):
    print(str(repeat(' ', star-1)) + "|")
