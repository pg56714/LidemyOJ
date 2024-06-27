# Array filter
# https://oj.lidemy.com/problem/1037
# 給你一個數列以及目標 target，若是數列中有符合 target 的元素，請把它刪除
# 第一行為要刪除的目標 target
# 第二行為一個數字 N，代表一共有幾個數字
# 接下來 N 行每行都是一個數字

# Sample Input
# 3
# 5
# 1
# 3
# 3
# 2
# 8

# Sample Output
# 1
# 2
# 8


def filter_array(numbers, target):
    filtered_numbers = [num for num in numbers if num != target]
    return filtered_numbers


target = int(input(""))

input_str = int(input(""))

numbers = []
for _ in range(input_str):
    number = int(input(""))
    numbers.append(number)

result = filter_array(numbers, target)

for number in result:
    print(number)
