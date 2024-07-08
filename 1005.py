# 題目：聯誼話題相親數
# https://oj.lidemy.com/problem/1005
# 例如說 220 的全部正因數（扣掉自己）相加是：1+2+4+5+10+11+20+22+44+55+110 = 284
# 而 284 的全部正因數（扣掉自己）相加總和是：1+2+4+71+142 = 220
# 只要符合這個特性，我們就稱作這兩數互為相親數。所以 220 與 284 是一組相親數。

# 輸入會有 M 個數字，彼此之間以空行分隔
# 若是碰到 0 代表輸入結束，請勿做任何處理

# 針對每一個輸入，請輸出它的相親數。
# 若是沒有相親數，請輸出 QQ

# Sample Input 1
# 220
# 221
# 222
# 223
# 0

# Sample Output 1
# 284
# QQ
# QQ
# QQ


def sum_of_proper_divisors(n):
    """計算並返回數字 n 的所有正因數（不包括 n 本身）的和"""
    if n < 2:
        return 0
    total = 1  # 1 是所有數字的因數
    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            total += i
            if i != n // i:  # n // i 是 i 的對稱因數，例如 i = 6, n // i = 6
                total += n // i
    return total


def find_amicable_number(num):
    """找出並返回數字 num 的相親數，如果沒有，返回 'QQ'"""
    sum1 = sum_of_proper_divisors(num)
    if sum1 == num or sum1 <= 1:
        return "QQ"
    sum2 = sum_of_proper_divisors(sum1)
    if sum2 == num:
        return sum1
    return "QQ"


while True:
    input_num = input().strip()
    if input_num == "0":
        break
    num = int(input_num)
    result = find_amicable_number(num)
    print(result)
