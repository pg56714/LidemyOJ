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


def reverse_array(input_str):
    numbers = []

    for _ in range(input_str):
        number = int(input(""))
        numbers.append(number)

    reversed_numbers = numbers[::-1]

    for number in reversed_numbers:
        print(number)


input_str = int(input(""))
reverse_array(input_str)
