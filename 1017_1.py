# 題目：貪婪的小偷
# 小偷想要偷較有價值的C樣物品，最後做一個加總

# 第一行數字(C)，代表小偷最多能夠帶走幾樣物品
# 第二行數字(N)，代表一共有幾項
# 從大到小排序，最後加總C樣物品

# 注意事項：有一個情況是想拿3樣，但實際只拿走1樣，那就是拿走1樣物品的價值
# https://oj.lidemy.com/problem/1017

take = int(input())  # C
if take <= 0:
    allNumber = 0
else:
    allNumber = int(input())  # N
ans = []

for i in range(allNumber):
    all = int(input())  # 每個物品的價值
    ans.append(all)

ans.sort(reverse=True)
total = 0

if take <= 0:
    print(total)
elif take >= allNumber:
    print(sum(ans))
else:
    for j in range(take):
        total += int(ans[j])  # 加總
    print(total)
