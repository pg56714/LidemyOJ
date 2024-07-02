# Yo！倒著唸！
# https://oj.lidemy.com/problem/1009

# 輸入會是一個字串 S

# Sample Input
# abcde

# Sample Output
# edcba


def reverse_string(s):
    # 方法一
    # return s[::-1]

    # 方法二
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


s = input("")
print(reverse_string(s))
