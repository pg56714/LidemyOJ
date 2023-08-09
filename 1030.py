# 題目：判斷迴文
# https://oj.lidemy.com/problem/1030

# 迴文的定義很簡單，就是你把一個字串倒過來以後還是長的跟原字串一樣
# 舉例來說，aba倒過來還是aba，我們就稱aba為迴文，abab就不是迴文

# 方法一
# n = input()


# def isRecover(n):
#     for i in range(len(n)):
#         if n[i] != n[len(n) - i - 1]:
#             return False
#     return True


# if isRecover(n):
#     print(True)
# else:
#     print(False)

# 方法二
n = input()
ans = ''

for i in reversed(range(len(n))):
    ans += n[i]

if n == ans:
    print(True)
else:
    print(False)
