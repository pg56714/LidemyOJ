# 題目：平面距離計算
# https://oj.lidemy.com/problem/1032
# 計算出兩個點的距離，公式 (絕對值(x1 - x2) 平方 + 絕對值(y1 - y2) 平方) 開根號，並四捨五入到小數點第二位

n = int(input())

all = []


def abs(n):
    # 絕對值
    if n < 0:
        return -n
    return n


for i in range(n * 4):
    all_Input = int(input())
    all.append(all_Input)
# print(all)

for i in range(n):
    x1 = all[i * 4 + 0]
    y1 = all[i * 4 + 1]
    x2 = all[i * 4 + 2]
    y2 = all[i * 4 + 3]

    distance = ((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5

    # '%.2f' % 四捨五入
    print('%.2f' % round(distance, 2))
