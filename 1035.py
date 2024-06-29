# 簡易排序
# https://oj.lidemy.com/problem/1035
# 第一行為一個數字 N
# 接下來 N 行每行都是一個正整數

# Sample Input
# 5
# 1
# 7
# 4
# 9
# 5

# Sample Output
# 1
# 4
# 5
# 7
# 9


# def easy_sort(numbers):
#     # 方法一
#     # results = []
#     # numbers.sort()

#     # for number in numbers:
#     #     results.append(number)

#     # return results

#     # 方法二
#     # 插入排序實現
#     for i in range(1, len(numbers)):
#         key = numbers[i]
#         # print(key)
#         j = i - 1
#         # 將選取的元素放到前面已排序部分的正確位置
#         while j >= 0 and key < numbers[j]:
#             numbers[j + 1] = numbers[j]
#             j -= 1
#         numbers[j + 1] = key
#     return numbers


# 方法三
# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


N = int(input())

# numbers = []
# for _ in range(N):
#     number = int(input())
#     numbers.append(number)
numbers = [int(input()) for _ in range(N)]

# result = easy_sort(numbers)
result = quick_sort(numbers)
for res in result:
    print(res)
