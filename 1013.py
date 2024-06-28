# 搭電梯
# https://oj.lidemy.com/problem/1013
# 電梯內部的系統壞掉了，對於樓層的判斷出錯，因此每一次只能往上一層樓或兩層樓，其餘的樓層都不會亮燈。

# 輸入為一個數字 N

# Sample Input
# 5

# Sample Output
# 5

# Hint
# 要到第五層樓，一共有以下五種方法：
# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 2 -> 3 -> 5
# 1 -> 2 -> 4 -> 5
# 1 -> 3 -> 4 -> 5
# 1 -> 3 -> 5


def ways_to_climb(n):
    # 方法一
    # if n == 2:
    #     return 1
    # if n == 3:
    #     return 2

    # dp = [0] * (n + 1)
    # # print(dp)
    # dp[0], dp[1], dp[2], dp[3] = 0, 1, 1, 2

    # for i in range(4, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]

    # return dp[n]

    # 方法二
    if n == 2:
        return 1
    if n == 3:
        return 2

    return ways_to_climb(n - 1) + ways_to_climb(n - 2)


n = int(input(""))
print(ways_to_climb(n))
