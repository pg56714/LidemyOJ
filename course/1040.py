# Array join
# https://oj.lidemy.com/problem/1040
# 給你一個數列以及要組合的字串 str，請輸出數列裡面每個元素與 str 組合而成的結果
# 舉例來說，假設有個數列是 1,2,3 而 str 是 !
# 組合完的結果就是：1!2!3，要注意的是 3 的後面不會有 str
# 換句話說，就是在每一個元素中間都插入 str，並且輸出成一個字串

# 第一行為要插入的目標 str
# 第二行為一個數字 N，代表一共有幾個數字
# 接下來 N 行每行都是一個數字

# Sample Input 1
# ,
# 3
# 1
# 2
# 3

# Sample Output 1
# 1,2,3

# Sample Input 2
# !!
# 3
# 1
# 2
# 3

# Sample Output 2
# 1!!2!!3


def manual_join(numbers, separator):
    # 方法一
    # result = ""
    # for i in range(len(numbers)):
    #     if i < len(numbers) - 1:
    #         result += str(numbers[i]) + separator
    #     else:
    #         result += str(numbers[i])
    # return result

    # 方法二
    result = str(numbers[0])
    for i in range(1, len(numbers)):
        result += separator + str(numbers[i])
    return result


separator = input("")

N = int(input(""))

numbers = []
for _ in range(N):
    number = int(input(""))
    numbers.append(number)

result = manual_join(numbers, separator)

print(result)
