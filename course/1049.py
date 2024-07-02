# 陣列最短距離
# https://oj.lidemy.com/problem/1049
# 已知兩個從小到大排好的陣列 x 與 y，求最短距離為何？
# 例如說 x 為 [1, 4, 5, 7, 9]，而 y 為 [3, 12, 15]
# 最短距離就是 1，因為 x[1] 與 y[0] 的距離為 1（4 - 3）

# 第一行會有兩個用空白分隔的正整數 n 與 m，分別代表陣列 x 與陣列 y 的元素個數
# 接著第二行會有 n 個用空白分隔的正整數，表示陣列 x 的元素
# 第三行會有 m 個用空白分隔的正整數，表示陣列 y 的元素

# Sample Input
# 5 5
# 1 9 12 15 18
# 3 6 10 11 12

# Sample Output
# 0

# Hint
# 最短距離發生在 x[2]=12與 y[4]=12，距離為 0


def min_distance(x, y):
    i, j = 0, 0
    min_dist = float("inf")

    while i < len(x) and j < len(y):
        current_dist = abs(x[i] - y[j])
        if current_dist < min_dist:
            min_dist = current_dist

        if x[i] < y[j]:
            i += 1
        else:
            j += 1

    return min_dist


n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(min_distance(x, y))
