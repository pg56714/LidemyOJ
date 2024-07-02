# Two sum
# https://oj.lidemy.com/problem/1050
# 給定一個都是正整數的陣列以及一個數字 target
# 保證在這陣列裡面你可以找到兩個數的和剛好為 target
# 答案只有一組，而且同一個 index 不能用兩遍，求這兩數的 index 為何？
# 例如說陣列為 [1, 3, 5, 7, 10]，target 為 11
# 答案就是 0 4，因為 arr[0] + arr[4] = 11

# 第一行為兩個用空白分隔的數 n 與 target
# n 代表陣列裡有幾個數字，target 代表你要尋找的目標
# 接下來第二行為用空白分隔的 n 個數，代表陣列裡面的 n 個元素

# Sample Input
# 5 3
# 1 7 9 8 2

# Sample Output
# 0 4

# Hint
# arr[0]=1, arr[4]=2，加起來為 3


def two_sum(numbers, target):
    num_dict = {}

    for i, num in enumerate(numbers):
        complement = target - num
        # print(num_dict, complement, i, num)

        # num_dict 這邊是判斷 key
        if complement in num_dict:
            return num_dict[complement], i
        num_dict[num] = i


n, target = map(int, input().split())
numbers = list(map(int, input().split()))

result = two_sum(numbers, target)
print(result[0], result[1])
