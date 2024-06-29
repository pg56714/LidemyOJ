# 搜尋數字
# https://oj.lidemy.com/problem/1047
# 給你一個由小到大排序好而且數字不重複的陣列 A 以及 M 個查詢，每個查詢都會給一個數字 P
# 對於每一個查詢，若是 P 在陣列 A 裡面，請輸出它的 index；若是不在，請輸出 -1

# 第一行為為一組用空白分隔的正整數 N 與 M
# N 代表陣列 A 裡面有多少個元素
# M 代表一共有幾個查詢
# 接下來 N 行每一行都會有一個正整數 Ai，代表陣列 A 裡面的第 i 個數，陣列 A 裡面不會有重複的數
# 再接下來會有 M 行，每行都有一個正整數 Pi，代表要查詢的數字

# Sample Input
# 5 3
# 1
# 2
# 3
# 4
# 5
# 100
# 3
# 6

# Sample Output
# -1
# 2
# -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(int(input()))

for _ in range(M):
    P = int(input())
    result = binary_search(A, P)
    print(result)
