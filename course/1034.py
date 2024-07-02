# 題目：凱薩加密
# https://oj.lidemy.com/problem/1034
# 往右移之後超出 z，那就從 a 再開始。
# 例如說 xray 搭配 N=3，會變成：audb，因為 x 往右移兩位是 z，在右移一位就變成 a 了，以此類推

n = int(input())
s = input()
ans = ''

for i in str(s):
    num = ord(i) - 97
    newNum = (num + n) % 26
    ans += chr(newNum + 97)

print(ans)
