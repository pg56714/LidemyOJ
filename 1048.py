# 最大連續和
# https://oj.lidemy.com/problem/1048
# 現在有一個都是整數的數列 A，例如說： 2, -3, 4, 10, -4, 7, 2, -5
# 一個數列可以有許多「子數列」，例如說 2, -3 或是 2, 4 其實都是子數列，甚至單一一個元素 2 或是 -5 也都是子數列
# 而「連續子數列」代表著順序必須是連著的，例如說前三個元素：2, -3, 4 就構成一個連續子數列，而 2, -3, 10 就不是一個連續的子數列

# 以上面這個數列來說，可以隨意舉出其中幾個連續的子數列：
# 2, -3, 4, 10, -4, 7, 2, -5
# 2, -3, 4
# 4, 10, -4, 7
# 4, 10, -4, 7, 2, -5
# 10, -4, 7
# 在所有連續子數列當中，請求出總和最大的值是多少
# 以上面的數列為例，總和最大的子數列為：4, 10, -4, 7, 2，總和為 19

# 第一行為一個數字 N，代表數列中有幾個元素
# 接下來 N 行每行都是一個數字 Ai，表示數列中第 i 個元素的值


# Sample Input
# 5
# 2
# -3
# 5
# -3
# 7

# Sample Output
# 9

# Hint
# [5, -3, 7] 的總和為 9


def max_subarray_sum(numbers):
    # 方法一
    # max_sum = float("-inf")

    # for i in range(len(numbers)):
    #     for j in range(i, len(numbers)):
    #         sum = 0
    #         for k in range(i, j + 1):
    #             sum += numbers[k]
    #         if sum > max_sum:
    #             max_sum = sum

    # return max_sum

    # 方法二
    # n = len(numbers)
    # max_sum = float("-inf")

    # for start in range(n):
    #     current_sum = 0
    #     for end in range(start, n):
    #         current_sum += numbers[end]
    #         if current_sum > max_sum:
    #             max_sum = current_sum

    # return max_sum

    # 方法三
    # current_max = global_max = numbers[0]
    # for num in numbers[1:]:
    #     current_max = max(num, current_max + num)
    #     global_max = max(global_max, current_max)
    # return global_max

    # 方法四
    current_max = global_max = numbers[0]
    for num in numbers[1:]:
        # print(num)
        if current_max + num > num:
            current_max = current_max + num
        else:
            current_max = num

        if global_max < current_max:
            global_max = current_max
    return global_max


N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

max_sum = max_subarray_sum(A)
print(max_sum)
