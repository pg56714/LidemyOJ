# 幾個水桶
# https://oj.lidemy.com/problem/1008
# ...
# 王國裡的工匠都是「2 的愛好者」，對於 2 這個數字有莫名的狂熱。因此，每個水桶的容量都是 2 的 n 次方。
# 最小的是 2^0 = 1，接著是 2^1 = 2，2^2 = 4，以此類推。
# 再接下來的水桶容量為 32, 64, 128...，而最大的水桶容量為 2147483648，
# 為了減輕那些去取水的士兵們的負重，國王希望每一次取水都能帶最少的水桶去，而且「每一個水桶一定都要裝滿」，
# 現在你已經知道要取水的單位了，請你幫忙算算看，最少需要帶幾個水桶。

# 輸入為一個數字 M

# Sample Input 1
# 20

# Sample Output 1
# 2

# Hint
# 20 單位的水，帶一個 16 的水桶加一個 4 的水桶即可，所以答案是 2


def min_buckets(M):
    # 方法一
    # 直接使用了 Python 的 bin() 函數來獲得二進位表示，並用 count('1') 來數有多少個 1
    # return bin(M).count("1")

    # # 方法二
    # # 先找到最大的水桶容量
    # bucket_capacity = 1
    # while bucket_capacity * 2 <= M:
    #     bucket_capacity *= 2

    # count = 0
    # remaining_water = M
    # # 從最大的水桶開始，盡可能使用水桶裝水
    # while remaining_water > 0:
    #     if bucket_capacity <= remaining_water:
    #         remaining_water -= bucket_capacity
    #         count += 1
    #     else:
    #         bucket_capacity //= 2

    # return count

    # 方法三
    # 直接將 M 轉為二進位，並計算有多少個 1
    # 往右移位，每次判斷最後一位是否為 1，若是則 sum + 1
    sum = 0
    while M > 0:
        sum += M & 1
        M >>= 1
    return sum


M = int(input(""))
print(min_buckets(M))
