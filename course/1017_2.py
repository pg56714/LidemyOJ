# 題目：貪婪的小偷
# 小偷想要偷較有價值的C樣物品，最後做一個加總

# 第一行數字(C)，代表小偷最多能夠帶走幾樣物品
# 第二行數字(N)，代表一共有幾項
# 從大到小排序，最後加總C樣物品

# 注意事項：有一個情況是想拿3樣，但實際只拿走1樣，那就是拿走1樣物品的價值
# https://oj.lidemy.com/problem/1017


take = int(input())
if take == 0:
    print(0)
else:
    items = sorted([int(input()) for i in range(int(input()))])
    total = sum(items[-take:])
    print(total)
