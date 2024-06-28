# 不合群的人
# https://oj.lidemy.com/problem/1016
# 遊戲開始的時候會由其他同學幫忙出題，而針對每個題目，都會有兩個選項 A 與 B，接著這五個同學就依照個人喜好選擇 A 或是 B。
# 例如說題目是：「你喜歡吃飯還是麵？」，A 是飯，B 是麵，這五個人的答案就有可能是 A B B A B，兩個人喜歡吃飯，三個人喜歡吃麵
# 因為喜歡吃麵的人比較多，所以喜歡吃飯的那兩個人就是不合群。
# 如果有六個同學，然後三個人喜歡吃飯三個人喜歡吃麵，兩邊勢均力敵，就代表沒有人不合群。
# 當然，若是大家喜歡吃的都一樣，那就皆大歡喜，也是沒有人不合群。

# 第一行為一個數字 N，代表遊玩人數
# 接下來 N 行每行為一個字母
# 若是沒有人不合群，請輸出：PEACE

# Sample Input 1
# 5
# A
# B
# B
# A
# B

# Sample Output 1
# 1
# 4

# Hint
# 第一個人與第四個人都選 A，其他三人都選 B，所以這兩人不合群


def find_outliers(choices):
    # count_A = choices.count("A")
    # count_B = choices.count("B")
    # result = []

    count_A = 0
    count_B = 0
    result = []

    for choice in choices:
        if choice == "A":
            count_A += 1
        elif choice == "B":
            count_B += 1

    if count_A == 0 or count_B == 0 or count_A == count_B:
        # return "PEACE"
        return ["PEACE"]

    # if count_A > count_B:
    #     minority = "B"
    # else:
    #     minority = "A"
    minority = "B" if count_A > count_B else "A"

    for index in range(N):
        if choices[index] == minority:
            result.append(index + 1)

    return result


N = int(input(""))

choices = []
for _ in range(N):
    choice = input("").strip()
    choices.append(choice)

result = find_outliers(choices)
# if isinstance(result, list):
#     for res in result:
#         print(res)
# else:
#     print(result)
for res in result:
    print(res)
