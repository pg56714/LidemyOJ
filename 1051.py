# 逆序數對
# https://oj.lidemy.com/problem/1051
# 假設 A 為：1, 9, 2, 7, 3
# (9, 2), (9, 7), (9, 3), (7, 3) 這四組都是逆序數對
# 給你一個數列 A，請求出逆序數對一共有幾組

# 第一行為一個數字 n，表示數列 A 的大小
# 接下來第二行為 n 個用空格分開的數字，表示數列 A 中的元素

# Sample Input
# 5
# 5 4 3 2 1

# Sample Output
# 10


def merge_count_split_inv(arr, temp_arr, left, mid, right):
    i = left  # 左序列的起始索引
    j = mid + 1  # 右序列的起始索引
    k = left  # 用於暫存數組的起始索引
    inv_count = 0

    # 條件來合併兩個子序列
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # 有逆序數對出現
            temp_arr[k] = arr[j]
            inv_count += mid - i + 1
            j += 1
        k += 1

    # 複製剩餘的左側元素到 temp_arr
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # 複製剩餘的右側元素到 temp_arr
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # 將排序後的數組複製回 arr
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_count_split_inv(arr, temp_arr, left, mid, right)

    return inv_count


n = int(input())
A = list(map(int, input().split()))

temp_arr = [0] * n
result = merge_sort_and_count(A, temp_arr, 0, n - 1)
print(result)

# 方法一
# def count_inversions(arr):
#     sum = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 sum += 1
#     return sum


# n = int(input())
# A = list(map(int, input().split()))

# result = count_inversions(A)
# print(result)
