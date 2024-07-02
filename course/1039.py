# Array fill
# https://oj.lidemy.com/problem/1039
# 給你一個數列以及目標 target，請你把數列中每一個元素都變成 target，並且輸出調整完的數列
# 第一行為要填充的數字 target
# 第二行為一個數字 N，代表一共有幾個數字
# 接下來 N 行每行都是一個數字

# Sample Input
# 10
# 3
# 1
# 2
# 3

# Sample Output
# 10
# 10
# 10


def fill_array(N, target):
    filled_array = [target] * N
    return filled_array


target = int(input(""))

N = int(input(""))

result = fill_array(N, target)

for item in result:
    print(item)
