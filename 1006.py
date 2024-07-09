# 題目：聯誼坐法排排看
# https://oj.lidemy.com/problem/1006

# 1 2
# 3 4
# 5 6
# 7 8

# (1, 2), (3, 4), (5, 6), (7, 8)
# (1, 3), (3, 5), (5, 7)
# (2, 4), (4, 6), (6, 8)

# 第一行為一個偶數 N，代表店裡的座位數，座位編號從 1 到 N
# 第二行為一個數字 M，代表已經被佔走的座位數目
# 接下來 M 行每一行都包含一個數字，代表被佔走的座位編號

# 請輸出小明跟小美若是想要相鄰入座的話，一共有幾種組合
# （小明與小美誰坐哪邊不重要，例如說「小明坐 1、小美坐 2」，與「小明坐 2、小美坐 1」視為同一種組合）

# Sample Input 1
# 8
# 2
# 4
# 5

# Sample Output 1
# 4

# Sample Input 2
# 6
# 0

# Sample Output 2
# 7

# Hint
# 第一組測資為題目的範例
# 第二組測資一共有 4 個座位，1 號被佔走以後可以坐的組合為兩組：(2, 4), (3, 4)


def count_adjacent_pairs(n, occupied_seats):
    count = 0
    occupied = {}

    for seat in occupied_seats:
        occupied[seat] = True

    # 檢查水平相鄰座位 (i, i+1)
    for i in range(1, n, 2):
        if not occupied.get(i, False) and not occupied.get(i + 1, False):
            count += 1
            # print(i, i + 1)

    # 檢查交錯位置 (奇數起始，如1和3，3和5)
    for i in range(1, n - 1, 2):
        if not occupied.get(i, False) and not occupied.get(i + 2, False):
            count += 1
            # print(i, i + 2)

    # 檢查交錯位置 (偶數起始，如2和4，4和6)
    for i in range(2, n - 1, 2):
        if not occupied.get(i, False) and not occupied.get(i + 2, False):
            count += 1
            # print(i, i + 2)

    return count


n = int(input())
m = int(input())
occupied_seats = [int(input()) for _ in range(m)]

print(count_adjacent_pairs(n, occupied_seats))
