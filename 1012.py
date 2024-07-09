# 題目：買一送一
# https://oj.lidemy.com/problem/1012

# 輸入為兩行正整數 A 與 B，分別代表第一罐以及第二罐飲料的價錢
# 請輸出兩行數字，第一個數字為「最大飲料價值」，第二個數字為「損失值」

# Sample Input 1
# 35
# 25

# Sample Output 1
# 70
# 10

# Hint
# 最大飲料價值為：35 *2 = 70
# 損失值為：70 - (35 + 25) = 10


def calculate_drink_values(A, B):
    max_price = max(A, B)

    max_value = max_price * 2

    loss_value = max_value - (A + B)

    return max_value, loss_value


A = int(input())
B = int(input())

max_value, loss_value = calculate_drink_values(A, B)

print(max_value)
print(loss_value)
