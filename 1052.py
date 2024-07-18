# 貪婪的小偷 Part2
# https://oj.lidemy.com/problem/1052

# 第一行為兩個用空白分隔的數字 N 與 W，分別代表物品數量以及背包能夠承受的重量
# 1 <= N <= 20, 1 <= W <= 100

# 接下來 N 行每行都有兩個以空白分隔的數字，分別是第 i 樣物品的重量 Wi 以及價值 Pi
# 1 <= Wi <= 100, 1 <= Pi <= 10000

# 請輸出小偷最多能偷到多少價值的東西

# Sample Input 1
# 3 10
# 9 100
# 5 60
# 2 70

# Sample Output 1
# 130

# Hint
# 背包重量為 10，可以偷到最大的價值為重量 5 的 60 + 重量 2 的 70，答案為 130
# 請放心地暴力解，或者是搜尋關鍵字：背包問題


# 暴力解法
# def knapsack_bruteforce(N, W, items):
#     max_value = 0

#     # 迭代所有可能的物品組合（2^N 種可能）
#     # << 是位元運算子，將 1 左移 N 位，相當於 2^N
#     for mask in range(1 << N):  # 1 << N 等於 2^N
#         # print(mask)
#         total_weight = 0
#         total_value = 0

#         # 檢查每一個物品是否被選中
#         for i in range(N):
#             # print(mask, i, mask & (1 << i))
#             if mask & (1 << i):
#                 weight, value = items[i]
#                 # print(weight, value)

#                 total_weight += weight
#                 total_value += value

#         # print(total_weight, total_value)
#         if total_weight <= W:
#             max_value = max(max_value, total_value)

#     return max_value


# 動態規劃解法
def knapsack(N, W, items):
    # dp[i][w] 表示考慮前 i 個物品，當背包容量為 w 時的最大價值
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    # print(dp)

    # 遍歷每個物品
    for i in range(1, N + 1):
        weight, value = items[i - 1]
        # print(weight, value)

        # 遍歷每種可能的背包容量
        for w in range(W + 1):
            # print(i, w)
            # 不選擇這個物品
            dp[i][w] = dp[i - 1][w]
            # 選擇這個物品（如果可以放入背包）
            if w >= weight:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)
            # print(i, w, weight, value, dp)

    # dp[N][W] 就是考慮所有物品，當背包容量為 W 時能得到的最大價值
    return dp[N][W]


N, W = map(int, input().split())
items = []
for _ in range(N):
    weight, value = map(int, input().split())
    items.append((weight, value))

# print(items)
max_value = knapsack(N, W, items)
# max_value = knapsack_bruteforce(N, W, items)
print(max_value)
