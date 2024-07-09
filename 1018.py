# 題目：大平台
# https://oj.lidemy.com/problem/1018

# 111, 222222222, 333333, 4444444
# 就代表著每一階層的長度，例如說第一階的長度為 3，第二階的長度為 9，第三階的長度為 6，第四階的長度為 7
# 第一行是一個正整數 N，代表一共有幾個數字
# 第二行會有 N 個以空白分隔的數字，已經由小到大排序好，代表每一個階層的長度
# 請你求出大平台（也就是長度最長的平台）的長度為何

# Sample Input 1
# 10
# 1 1 2 2 2 3 3 3 4 4

# Sample Output 1
# 3

# Hint
# 第二階：222 以及第三階：333 皆為大平台，長度為 3


def find_longest_platform(n, lengths):
    max_length = 1
    current_length = 1

    for i in range(1, n):
        if lengths[i] == lengths[i - 1]:
            current_length += 1
        else:
            current_length = 1

        if current_length > max_length:
            max_length = current_length

    return max_length


n = int(input())
lengths = list(map(int, input().split()))

result = find_longest_platform(n, lengths)
print(result)
