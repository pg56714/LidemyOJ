# String trim
# https://oj.lidemy.com/problem/1041
# 給你一個字串 S，請輸出把頭尾的空格去掉之後的結果（只有頭尾，在字串中間的不算）
# 輸入只有一行，為一個字串 S

# Sample Input 1
#       a b c

# Sample Output 1
# a b c

# Sample Input 2
#   abc

# Sample Output 2
# abc


def manual_trim(s):
    # 方法一
    # start = 0
    # while start < len(s) and s[start] == " ":
    #     start += 1

    # end = len(s) - 1
    # while end >= 0 and s[end] == " ":
    #     end -= 1

    # # print(start, end)
    # if start > end:
    #     return ""

    # return s[start : end + 1]

    # 方法二
    result = ""
    isFrontWhiteSpaceEnd = False
    for char in s:
        if char != " " or isFrontWhiteSpaceEnd:
            isFrontWhiteSpaceEnd = True
            result += char

    ret = ""
    isBackWhiteSpaceEnd = False
    for i in range(len(result) - 1, -1, -1):
        if result[i] != " " or isBackWhiteSpaceEnd:
            isBackWhiteSpaceEnd = True
            ret = result[i] + ret

    return ret


input_string = input("")

trimmed_string = manual_trim(input_string)
print(trimmed_string)
