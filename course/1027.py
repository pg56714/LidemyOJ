# 題目：信用卡驗證
# https://oj.lidemy.com/problem/1027
# 為了節省大家的麻煩，這一題的測試資料卡號皆為 16 碼，Master Card 是 5 開頭，Visa 是 4，JCB 則是 3。
# 前 15 位數經過加權後加總，會得出一個數字，先把這數字除以 10 取餘數，如果結果是 0，那檢查碼就是 0，否則就是用 10 減去之後的結果
# 權重的部分你可以很簡單這樣記：左邊數起奇數位是 2，偶數位是 1
# 若是在計算的過程中某一位數加權後的結果比 10 大，那請減去 9

# 舉例來說，5412-3456-7890-1232這個卡號的第一位是 5，代表這是 MasterCard 的卡
# 而奇數位加總為：5*2 + 1*2 + 3*2 + 5*2 + 7*2 + 9*2 + 1*2 + 3*2，原本應該是：10 + 2 + 6 + 10 + 14 + 18 + 2 + 6
# 但前面有說過「如果比 10 大，請減去 9」，所以就是 1(10-9) + 2 + 6 + 1(10-9) + 5(14-9) + 9(18-9) + 2 + 6 = 32
# 偶數位加總為：4 + 2 + 4 + 6 + 8 + 0 + 2 = 26，乘以 1 之後還是 26
# 把 32 跟 26 相加，得到 58，58 % 10 = 8，因此檢查碼就是 10-8 = 2
# 而卡號的第 16 碼也是 2，因此這個卡號是沒有問題的。

input = input().split('-')
n = input[0] + input[1] + input[2] + input[3]


def isValid(n):
    sum = 0  # 加總
    sum_1 = 0  # 奇
    sum_2 = 0  # 偶

    for i in range(len(n)-1):
        # print(i)

        if i % 2 == 0:
            if (int(n[i]) * 2 >= 10):
                sum_1 += (int(n[i]) * 2 - 9)
            else:
                sum_1 += (int(n[i]) * 2)
            # print('奇數：', n[i])
        else:
            sum_2 += int(n[i])
            # print('偶數：', n[i])
    sum = (sum_1 + sum_2) % 10
    if sum != 0:
        sum = 10 - sum

    # print(sum_1)
    # print(sum_2)
    # print(sum)
    # print(n[-1])

    if int(n[-1]) == sum:
        return True
    else:
        return False


if isValid(n):
    if int(n[0]) == 5:
        print('MASTER_CARD')
    elif int(n[0]) == 4:
        print('VISA')
    # elif int(n[0]) == 3:
    #     print('JCB')
else:
    print('INVALID')
