# Array reverse
# https://oj.lidemy.com/problem/1036
# Reverse 是許多程式語言對於陣列都會內建的功能，可以把一個陣列反轉
# 第一行為一個數字

# Sample Input
# 3
# 1
# 2
# 3

# Sample Output
# 3
# 2
# 1


def reverse_array(numbers):
    # 方法一
    # reversed_numbers = numbers[::-1]

    # 方法二
    reversed_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[i])

    return reversed_numbers


input_str = int(input(""))

numbers = []
for _ in range(input_str):
    number = int(input(""))
    numbers.append(number)

result = reverse_array(numbers)
# print(result)
for number in result:
    print(number)
