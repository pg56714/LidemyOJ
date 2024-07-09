# 題目：183 Club
# https://oj.lidemy.com/problem/1011

# 第一行為一個數字 M，代表底下有幾筆身高
# 第二行為 M 個用空格分開的正整數
# 若是成員的平均身高大於等於 183，請輸出：「real」，反之則輸出「fake」

# Sample Input 1
# 5
# 180 181 182 183 184

# Sample Output 1
# fake


def is_club_real_or_fake(m, heights):
    average_height = sum(heights) / m

    if average_height >= 183:
        return "real"
    else:
        return "fake"


m = int(input())
heights = list(map(int, input().split()))

result = is_club_real_or_fake(m, heights)
print(result)
