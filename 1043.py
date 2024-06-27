# String endsWith
# https://oj.lidemy.com/problem/1043
# 給定兩個字串 S 與 target，請判斷 S 是不是以 target 結尾
# 例如說 S=abc，target=c，abc 是以 c 結尾沒錯，答案就是 true
# 或者 S=abc，target=bc 或是 target=abc，答案也都是 true
# 輸入有兩行
# 第一行為一個字串 S
# 第二行為一個字串 target

# Sample Input 1
# abcde
# f

# Sample Output 1
# false

# Sample Input 2
# aaa
# aa

# Sample Output 2
# true


def ends_with(s, target):
    if len(target) > len(s):
        return False

    # 方法一
    # start_index = len(s) - len(target)
    # if s[start_index:] == target:
    #     return True
    # else:
    #     return False

    # 方法二
    index_s = len(s) - 1
    index_target = len(target) - 1

    while index_target >= 0:
        if s[index_s] != target[index_target]:
            return False
        index_s -= 1
        index_target -= 1

    return True


s = input("")
target = input("")

if ends_with(s, target):
    print("true")
else:
    print("false")
