# Array indexOf
# https://oj.lidemy.com/problem/1038
# 給你一個數列以及目標 target，若是數列中有符合 target 的元素，請輸出它的 index，若是沒有，請輸出 -1
# 第一行為要尋找的目標 target
# 第二行為一個數字 N，代表一共有幾個數字
# 接下來 N 行每行都是一個數字

# Sample Input
# 3
# 5
# 1
# 2
# 3
# 3
# 3

# Sample Output
# 2


def find_first_index(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


target = int(input(""))

input_str = int(input(""))

numbers = []
for _ in range(input_str):
    number = int(input(""))
    numbers.append(number)

result = find_first_index(numbers, target)
print(result)
