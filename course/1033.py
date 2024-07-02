# 題目：最近點對
# https://oj.lidemy.com/problem/1033
# 先計算出兩個點的距離，公式 ((x1 - x2) 平方 + (y1 - y2) 平方) 開根號
# 輸出的時候請先輸出 x 比較小的那個點，若是 x 相同，請先輸出 y 比較小的那個點

# 測資
# 4(筆)
# 2 3
# 1 3
# 1 2
# 1 1

# 2 3 1 3 1 2 1 1(存陣列)
# 0 1 2 3 4 5 6 7

n = int(input())

all = []


def abs(n):
    # 絕對值
    if n < 0:
        return -n
    return n


# 先儲存輸入資料到陣列
for i in range(n):
    all_Input = (input().split(' '))
    all.append(all_Input[0])
    all.append(all_Input[1])

# print(all)


def countDistance(i, j):
    x1 = int(all[i * 2 + 0])  # 0、2、4
    y1 = int(all[i * 2 + 1])  # 1、3、5
    x2 = int(all[j * 2 + 0])  # 2、4、6
    y2 = int(all[j * 2 + 1])  # 3、5、7

    # 計算距離
    distance_1 = ((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5
    input_1 = [x1, y1, x2, y2]
    return distance_1, input_1


def find_min_input(n):
    for q in range(n):
        for k in range(q+1, n):
            if q == 0 and k == 1:
                # 先存第一筆
                min_distance, min_input = countDistance(q, k)
                # print('1：', min_distance, min_input)
            else:
                # 1、2，2、3，3、4，4、5，5、6，6、7
                distance_2, input_2 = countDistance(q, k)
                # print('2：', distance_2, input_2)

                # 與第一筆資料比較大小
                if distance_2 < min_distance:
                    min_distance = distance_2
                    min_input = input_2
    # print(min_input)
    return min_input


def output(min_input_1):
    # 輸出的時候請先輸出 x 比較小的那個點，若是 x 相同，請先輸出 y 比較小的那個點
    if min_input_1[0] == min_input_1[2]:
        if min_input_1[1] < min_input_1[3]:
            print(min_input_1[0], min_input_1[1])
            print(min_input_1[2], min_input_1[3])
        else:
            print(min_input_1[2], min_input_1[3])
            print(min_input_1[0], min_input_1[1])
    else:
        # 2 < 1
        if min_input_1[0] < min_input_1[2]:
            print(min_input_1[0], min_input_1[1])
            print(min_input_1[2], min_input_1[3])
        else:
            print(min_input_1[2], min_input_1[3])
            print(min_input_1[0], min_input_1[1])


min_point_2 = find_min_input(n)
output(min_point_2)
