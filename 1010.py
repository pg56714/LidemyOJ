# 題目：靈魂伴侶
# 兩個用空格分隔的正整數，若兩數相等輸出Yes，否則No
# https://oj.lidemy.com/problem/1010

import sys
str = sys.stdin.readline().strip('\n')
tmp = str.split()

if (int(tmp[0]) == int(tmp[1])):
    print("Yes")
else:
    print("No")
