# 題目：聯誼門票搶起來
# https://oj.lidemy.com/problem/1003
# 一開始會給一個數字 n，後面跟著 n 行字串：
# 3
# hello
# world
# yo

# 把這些字串拼起來，就會變成一個更長的字串 S，以上面的範例來說，S 就是 helloworldyo。
# 接著會給一個數字 m，代表接下來有 m 個用空行分隔的數字 ，例如說：
# 2
# 9
# 1

# 就代表要把第 9 個字還有第 1 個字合起來（字串的第一個字就是第一個字，不是第零個字）
# helloworldyo 的第九個字元是：l
# helloworldyo 的第一個字元是：h
# 因此答案就是：lh

# Sample Input 1
# 2
# yo
# man
# 3
# 4
# 2
# 1

# Sample Output 1
# aoy


def fetch_characters(combined_string, query_count):
    result = ""
    for _ in range(query_count):
        position = int(input()) - 1
        result += combined_string[position]
    return result


n = int(input())

S = ""
for _ in range(n):
    S += input()

m = int(input())

result = fetch_characters(S, m)
print(result)
