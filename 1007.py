# 題目：聯誼排行大比拼
# https://oj.lidemy.com/problem/1007

# 第一行為一個數字 M，代表以下有幾組資料
# 底下每一組資料都會包含一個人名 N 以及好感度總和 S，會用空格隔開
# 請輸出人氣王的名字，若是有兩位以上的人氣王，請依據出現在輸入裡面的順序依序輸出

# Sample Input 1
# 3
# Nick 8
# Peter 5
# Nic 100

# Sample Output 1
# Nic

# Sample Input 2
# 3
# Nick 90
# Peter 90
# Bob 80

# Sample Output 2
# Nick
# Peter

# Hint
# 第一組測資 Nic 為人氣王
# 第二組測資 Nick 與 Peter 同時為人氣王，所以按照輸入的順序依序輸出 Nick 與 Peter


def find_popularity_king(m, data):
    popularity = []

    for i in range(m):
        name, score = data[i]
        score = int(score)
        popularity.append((name, score))

    # key=lambda x: x[1] ， 例如 popularity = [('Nick', 8), ('Peter', 5), ('Nic', 100)]
    # 則 max(popularity, key=lambda x: x[1]) 會回傳 ('Nic', 100)[1] = 100
    max_score = max(popularity, key=lambda x: x[1])[1]

    kings = [name for name, score in popularity if score == max_score]

    return kings


m = int(input())
data = [input().split() for _ in range(m)]

result = find_popularity_king(m, data)

for king in result:
    print(king)
