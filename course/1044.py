# String padEnd
# https://oj.lidemy.com/problem/1044
# pad 翻作「填充」，而 padEnd 顧名思義就是在字串的尾端填充字元
# 會有兩個參數 length 以及 str，代表預期字串最後的長度，以及要填充的字串是什麼
# 例如說現在有個字串 S=abc，length=5，str=a，填充完就會變成 abcaa
# a 會重複兩次，因為還沒到達預期的長度
# 或者是 S=abc，length=5，str=abcdefghijk，填充完會是 abcab
# str 後面的字串會被截斷，因為長度已經到了規定的 5 個字
# 有一種特殊情況是 S 的長度已經大於等於 length，例如說 S=abc，length=1，str=zzz，結果就會是原字串 S，不會做任何改動

# 輸入的第一行為一個字串 S
# 第二行為預期的長度 length
# 第三行為一個字串 str


# Sample Input 1
# abcaa
# 10
# xyz

# Sample Output 1
# abcaaxyzxy

# Sample Input 2
# abcaa
# 5
# xyz

# Sample Output 2
# abcaa


def pad_end(s, length, pad_str):
    if len(s) >= length:
        return s

    # 方法一
    # needed_length = length - len(s)

    # full_repeats = (needed_length // len(pad_str)) + 1
    # full_pad = pad_str * full_repeats

    # final_pad = full_pad[:needed_length]

    # return s + final_pad

    # # 方法二
    # result = s
    # while len(result) < length:
    #     result += pad_str
    # new_result = ""

    # for i in range(length):
    #     new_result += result[i]

    # return new_result

    # 方法三
    result = s
    n = 0
    while len(result) < length:
        result += pad_str[n]
        n += 1
        if n == len(pad_str):
            n = 0

    return result


s = input("")
length = int(input(""))
pad_str = input("")

result = pad_end(s, length, pad_str)
print(result)
