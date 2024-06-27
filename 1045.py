# String slice
# https://oj.lidemy.com/problem/1045
# slice 通常用來取陣列或者是字串的其中一部分，有兩個參數 start 與 end
# 提取範圍是 start 到 end - 1
# 例如說對 str=abcdef，start=1，end=5，答案就是 bcde
# 雖然在實際使用中可以省略 end 或者是傳負數，但在這題我們暫時不考慮這種情形

# 第一行為一個字串 S
# 第二行為一個數字 start
# 第三行為一個數字 end


# Sample Input 1
# abcde
# 0
# 3

# Sample Output 1
# abc


def slice_string(s, start, end):
    # 方法一
    # return s[start:end]

    # 方法二
    result = ""
    for i in range(start, end):
        result += s[i]
    return result


s = input("")
start = int(input(""))
end = int(input(""))

result = slice_string(s, start, end)
print(result)
