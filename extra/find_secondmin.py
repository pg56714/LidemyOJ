# 找陣列次小值

arr = [1, 2, 6, 7, 8, 9, 5, 4, 3]

# 最小值 min_1 設為 max 為陣列中的最大值
min_1 = arr[arr.index(max(arr))]  # 最小值
min_2 = arr[arr.index(max(arr))]  # 次小值

for i in range(len(arr)):
    # print(min_1)
    # print(min_2)
    # print('---')
    if arr[i] < min_1:

        min_2 = min_1
        min_1 = arr[i]

    elif arr[i] < min_2:
        min_2 = arr[i]

print(min_2)
