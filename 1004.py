# 題目：聯誼順序比大小
# https://oj.lidemy.com/problem/1004
# 輸入第一行會是一個數字 M，代表一共有幾組比賽的結果
# 接著每一行會有三個用空白分隔的數字 A, B, K
# A 代表 A 選擇的數字，B 代表 B 選擇的數字，兩者皆保證為正整數
# 要特別注意的是 A 與 B 可能是很大的數字，但保證長度為 512 個位數以內

# K 只會有兩種情況：1 或是 -1，若是 1 代表數字大的獲勝，K 若是 -1 代表數字小的獲勝
# 若是 A 贏請輸出 A，B 贏請輸出 B，平手則輸出 DRAW

# Sample Input 1
# 3
# 1 2 1
# 1 2 -1
# 2 2 1

# Sample Output 1
# B
# A
# DRAW


def determine_winner(M):
    results = []
    for _ in range(M):
        A, B, K = map(int, input().split())
        if K == 1:
            if A > B:
                results.append("A")
            elif A < B:
                results.append("B")
            else:
                results.append("DRAW")
        elif K == -1:
            if A < B:
                results.append("A")
            elif A > B:
                results.append("B")
            else:
                results.append("DRAW")
    return results


M = int(input())
result = determine_winner(M)

for winner in result:
    print(winner)
